from dotenv import load_dotenv
import os

if os.path.exists(".env.local"):
    load_dotenv(".env.local")
elif os.path.exists(".env.docker"):
    load_dotenv(".env.docker")
else:
    load_dotenv()
    
import json
import logging
from neo4j import GraphDatabase

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

RELATION_PREDICATES = {
    "has_enum": "HAS_ENUM",
    "is_friend_with": "IS_FRIEND_WITH",
    "is_method_of": "IS_METHOD_OF",
    "has_attribute": "HAS_ATTRIBUTE",
    "belongs_to_enum": "BELONGS_TO_ENUM",
    "belongs_to_class": "BELONGS_TO_CLASS",
    "is_attribute_of": "IS_ATTRIBUTE_OF",
    "returns": "RETURNS_TYPE",
    "belongs_to_dict": "BELONGS_TO_DICT",
    "uses_dictionary": "USES_DICTIONARY"
}
PROPERTY_PREDICATES = [
    "has_value", "has_description", "has_code", "has_type", "stores", "accesses", "has_argument_type", "has_symbol", "may_contain_fields"
    ]

def normalize_label(label):
    return label.upper()

def node_label_from_type(obj_type):
    if obj_type == "class":
        return "Class"
    if obj_type == "enum":
        return "Enum"
    if obj_type == "enum_value":
        return "EnumValue"
    if obj_type == "method":
        return "Method"
    if obj_type == "attribute":
        return "Attribute"
    if obj_type == "datatype":
        return "Datatype"
    if obj_type == "dictionary":
        return "Dictionary"
    if obj_type == "particle_code":
        return "ParticleCode"
    if obj_type == "reaction_code":
        return "ReactionCode"  
    if obj_type == "zaid_code":             
        return "ZAIDCode"
    if obj_type == "lookup_table":
        return "LookupTable"
    return None 

class Neo4jTripletMigrator:
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="decima123"):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None

    def connect(self):
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
            with self.driver.session() as session:
                session.run("RETURN 1")
            logger.info("Connexion à Neo4j établie avec succès")
            return True
        except Exception as e:
            print("❌ Could not connect to Neo4j. Make sure Neo4j Desktop is installed and running on bolt://localhost:7687.")
            logger.error(f"Erreur de connexion à Neo4j: {str(e)}")
            return False

    def close(self):
        if self.driver:
            self.driver.close()
            logger.info("Connexion à Neo4j fermée")

    def create_constraints(self):
        constraints = [
            "CREATE CONSTRAINT IF NOT EXISTS FOR (n:Entity) REQUIRE n.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (c:Class) REQUIRE c.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (e:Enum) REQUIRE e.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (ev:EnumValue) REQUIRE ev.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (m:Method) REQUIRE m.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (a:Attribute) REQUIRE a.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (pc:ParticleCode) REQUIRE pc.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (d:Dictionary) REQUIRE d.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (rc:ReactionCode) REQUIRE rc.name IS UNIQUE",
            "CREATE CONSTRAINT IF NOT EXISTS FOR (z:ZAIDCode) REQUIRE z.name IS UNIQUE",
        ]
        with self.driver.session() as session:
            for constraint in constraints:
                try:
                    session.run(constraint)
                except Exception as e:
                    logger.warning(f"Contrainte déjà existante ou erreur : {str(e)}")

    def create_or_update_node(self, session, name, label, properties=None):
        if not label:
            logger.warning(f"[SKIP] Tentative de création d'un nœud sans label: {name}")
            return
        props = ", ".join([f"{k}: ${k}" for k in (properties or {})])
        cypher = f"MERGE (n:{label} {{name: $name}})"
        if props:
            cypher += f"\nSET " + ", ".join([f"n.{k} = ${k}" for k in properties])
        session.run(cypher, name=name, **(properties or {}))
        print(f"Création ou update noeud [{label}] : {name} | Props: {properties}")

    def migrate_all_triplets(self, triplets_dir):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        self.create_constraints()
        files = [f for f in os.listdir(triplets_dir) if f.endswith(".json")]

        all_triplets = []
        for file in files:
            with open(os.path.join(triplets_dir, file), "r", encoding="utf-8") as f:
                all_triplets.extend(json.load(f))

        global_node_types = {}
        for triplet in all_triplets:
            subj = triplet["Subject"]
            pred = triplet["Predicate"]
            obj = triplet["Object"]
            if pred == "type":
                global_node_types[subj] = obj

        print("==== Node types extraits (global) ====")
        for k, v in global_node_types.items():
            print(f"  {k} -> {v}")

        with self.driver.session() as session:
            for node, obj_type in global_node_types.items():
                label = node_label_from_type(obj_type)
                if label:
                    self.create_or_update_node(session, node, label)
                else:
                    print(f"[IGNORE] Nœud sans label pour : {node}")

            for triplet in all_triplets:
                subj = triplet["Subject"]
                pred = triplet["Predicate"]
                obj = triplet["Object"]

                if pred == "type":
                    continue  

                if pred in PROPERTY_PREDICATES:
                    label = node_label_from_type(global_node_types.get(subj, None))
                    if label:
                        print(f"  Ajout propriété à {subj} (label {label}): {pred.replace('has_','')} = {obj}")
                        session.run(
                            f"MATCH (n:{label} {{name: $name}}) SET n.{pred.replace('has_', '')} = $value",
                            name=subj, value=obj
                        )
                    else:
                        print(f"[WARNING] Propriété pour {subj} ignorée car label introuvable")
                    continue

                if pred == "has_enum":
                    subj_label = node_label_from_type(global_node_types.get(subj, None))
                    obj_label = "Enum"
                    print(f"  Relation HAS_ENUM : {subj} ({subj_label}) -> {obj} (Enum)")
                    session.run(
                        f"""
                        MERGE (a:{subj_label} {{name: $subj}})
                        MERGE (b:{obj_label} {{name: $obj}})
                        MERGE (a)-[r:HAS_ENUM]->(b)
                        """,
                        subj=subj, obj=obj
                    )
                    continue

                if pred == "belongs_to_enum":
                    subj_label = node_label_from_type(global_node_types.get(subj, None))
                    obj_label = "Enum"
                    print(f"  Relation BELONGS_TO_ENUM : {subj} ({subj_label}) -> {obj} (Enum)")
                    session.run(
                        f"""
                        MERGE (a:{subj_label} {{name: $subj}})
                        MERGE (b:{obj_label} {{name: $obj}})
                        MERGE (a)-[r:BELONGS_TO_ENUM]->(b)
                        """,
                        subj=subj, obj=obj
                    )
                    continue

                rel_label = RELATION_PREDICATES.get(pred, normalize_label(pred))
                subj_label = node_label_from_type(global_node_types.get(subj, None))
                if not isinstance(obj, str):
                    print(f"[SKIP] Relation non supportée (objet complexe): {subj} --{pred}--> {obj} (type {type(obj)})")
                    continue
                obj_label = node_label_from_type(global_node_types.get(obj, None))
                if subj_label and obj_label:
                    print(f"  Relation {rel_label} : {subj} ({subj_label}) -> {obj} ({obj_label})")
                    session.run(
                        f"""
                        MERGE (a:{subj_label} {{name: $subj}})
                        MERGE (b:{obj_label} {{name: $obj}})
                        MERGE (a)-[r:{rel_label}]->(b)
                        """,
                        subj=subj, obj=obj
                    )
                else:
                    print(f"[WARNING] Impossible de relier {subj} (label={subj_label}) à {obj} (label={obj_label}) pour la relation {rel_label}")

        logger.info("Migration complète des triplets terminée.")

def main():
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASSWORD", "decima123")
    triplets_dir = os.getenv("TRIPLETS_DIR", os.path.join("kg", "triplets"))

    migrator = Neo4jTripletMigrator(uri, user, password)
    if migrator.connect():
        migrator.migrate_all_triplets(triplets_dir)
        migrator.close()

if __name__ == "__main__":
    main()


def get_neo4j_driver(uri=None, user=None, password=None):
    uri = uri or "bolt://localhost:7687"
    user = user or "neo4j"
    password = password or "decima123"
    return GraphDatabase.driver(uri, auth=(user, password))    
