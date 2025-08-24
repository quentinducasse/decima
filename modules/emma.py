"""
DECIMA Agent - EMMA - Engine for Metadata Mapping & Analysis
Knowledge Graph inference engine for extracting and ranking entities relevant to PTRAC queries
"""
from dotenv import load_dotenv
import os

if os.path.exists(".env.local"):
    load_dotenv(".env.local")
elif os.path.exists(".env.docker"):
    load_dotenv(".env.docker")
else:
    load_dotenv()
    
import os
import re
import sys
from neo4j import GraphDatabase
from typing import Dict, List, Any
from utils.keywords_fr_en import FR_TO_EN_LEXICON
from utils.keywords_quiet import FOCUS_DICTIONARIES
from modules.quiet import QUIET
from kg.loader.neo4j_loader import get_neo4j_driver

MT_PATTERN = re.compile(r'\bMT[\s_]?(\d{1,3})\b', re.IGNORECASE)
MT_NUMBER_PATTERN = re.compile(r'\b(\d{1,3})\b')
PARTICLE_NAMES = [
    "neutron", "photon", "proton", "triton", "deuteron", "alpha", "electron", "positron", "gamma", "helium", "3he", "4he"
]

def normalize(s):
    return s.replace("-", "").replace(" ", "").lower()

def print_llm_context(kg_context):
    print("\n[KG_CONTEXT LLM READY]")
    for ent in kg_context.get("entities", []):
        fields = [f"id: {ent['id']}"]
        if ent.get("type"):
            fields.append(f"type: {ent['type']}")
        if ent.get("focus_type"):
            fields.append(f"focus_type: {','.join(ent['focus_type'])}")
        if ent.get("parent_class"):
            fields.append(f"parent_class: {ent['parent_class']}")
        if ent.get("parent_enum"):
            fields.append(f"parent_enum: {ent['parent_enum']}")
        if ent.get("parent_dict"):
            fields.append(f"parent_dict: {ent['parent_dict']}")
        if ent.get("value") is not None:
            fields.append(f"value: {ent['value']}")
        if ent.get("score") is not None:
            fields.append(f"score: {ent['score']}")
        desc = ent.get("description", "")
        if desc:
            fields.append(f"description: {desc.strip().replace(chr(10),' ')[:150]}")
        print("- " + ", ".join(fields))


def extract_mt_numbers_from_query(query):
    mt_nums = set()
    for match in MT_PATTERN.finditer(query):
        mt_nums.add(match.group(1))
    if "mt" in query.lower() or "reaction" in query.lower():
        mt_nums.update(MT_NUMBER_PATTERN.findall(query))
    return {int(mtn) for mtn in mt_nums}

def tokens_match(kw, token):
    return kw == token or kw.rstrip('s') == token.rstrip('s') or kw in token or token in kw


def extract_reaction_patterns_from_query(query):
    patterns = set()
    # (n,p) ou (n,3a)...
    for match in re.findall(r"\((n,[^)\s]+)\)", query, flags=re.IGNORECASE):
        patterns.add(match.lower().replace(" ", ""))
    # n,p ou n,3a sans parenthèses, espace/virgule tolérés
    for match in re.findall(r"\bn[, ]\w+\b", query, flags=re.IGNORECASE):
        patterns.add(match.lower().replace(" ", ","))
    # Motif n,lettres+chiffres
    for match in re.findall(r"n,[a-z0-9α]+", query, flags=re.IGNORECASE):
        patterns.add(match.lower())
    return patterns

def print_entity(entity):
    print(f"\nID: {entity['id']} (type: {entity['type']})")
    typ = (entity.get('type') or '').lower()
    if typ == "enumvalue":
        print(f"  Parent enum: {entity.get('parent_enum')}")
        print(f"  Parent class: {entity.get('parent_class')}")
    elif typ == "enum":
        print(f"  Parent class: {entity.get('parent_class')}")
    elif typ == "class":
        pass
    elif typ == "method" or typ == "attribute":
        print(f"  Parent class: {entity.get('parent_class')}")
    if entity.get('parent_dict'):
        print(f"  Parent dict: {entity['parent_dict']}")
    if entity.get('description'):
        print(f"  Description: {entity['description']}")
    if entity.get("focus_type"):
        print(f"  Matched by QUIET: {entity['focus_type']}")

def score_mt_entity(mt_entity, query_keywords, focus_particles, query_mt_numbers, reaction_patterns_in_query=None):
    score = 0
    debug_info = []
    desc = (mt_entity.get("desc") or "")
    label = (mt_entity.get("label") or "")
    desc_norm = normalize(desc)
    label_norm = normalize(label)
    mt_id = mt_entity["id"]
    mt_num = int(mt_id.replace("MT_", "")) if mt_id.startswith("MT_") and mt_id[3:].isdigit() else None

    if mt_num and mt_num in query_mt_numbers:
        score += 100
        debug_info.append("MT# explicit (+100)")

    for part in focus_particles:
        n_part = normalize(part)
        if n_part in desc_norm or n_part in label_norm:
            score += 10
            debug_info.append(f"particle {part} (+10)")

    if reaction_patterns_in_query:
        for pattern in reaction_patterns_in_query:
            if pattern in desc_norm or pattern in label_norm:
                score += 30
                debug_info.append(f"pattern '{pattern}' (+30)")

    general_keywords = {
        "fission": {"fission", "fissions", "fissionnée", "fissionnées", "scission"},
        "capture": {"capture", "captures", "capturés", "capturées", "capturee", "capturée"},
        "elastic": {"elastic", "elastique", "elastiques", "élastique", "élastiques"},
        "inelastic": {"inelastic", "inelastique", "inelastiques", "inélastique", "inélastiques"},
    }

    query_keywords_norm = set(normalize(kw) for kw in query_keywords)
    # print(f"[DEBUG] Normalized query keywords: {query_keywords_norm}")

    for en_kw, variants in general_keywords.items():
        cited = any(normalize(v) in query_keywords_norm for v in variants)
        n_kw = normalize(en_kw)
        if n_kw in desc_norm or n_kw in label_norm:
            if cited:
                score += 20
                debug_info.append(f"{en_kw} cited (+20)")
            else:
                score += 5
                debug_info.append(f"{en_kw} not cited (+5)")


    for kw in query_keywords_norm:
        if kw in desc_norm or kw in label_norm:
            score += 2
    # if score > 0:
    #     print(f"[DEBUG MT] {mt_id}: score={score} | {'; '.join(debug_info)}")
    return score


class EMMA:
    def __init__(self, neo4j_uri=None, neo4j_user=None, neo4j_password=None):
        self.driver = get_neo4j_driver(
            uri=neo4j_uri or os.getenv("NEO4J_URI", "bolt://localhost:7687"),
            user=neo4j_user or os.getenv("NEO4J_USER", "neo4j"),
            password=neo4j_password or os.getenv("NEO4J_PASSWORD", "neo4j")
        )

    def close(self):
        self.driver.close()

    def get_entity_full_info(self, session, entity_id):
        cypher = """
        MATCH (n {name: $entity_id})
        OPTIONAL MATCH (n)-[:BELONGS_TO_ENUM]->(enum:Enum)
        OPTIONAL MATCH (enum)<-[:HAS_ENUM]-(class:Class)
        OPTIONAL MATCH (n)<-[:HAS_ENUM]-(class2:Class)
        OPTIONAL MATCH (n)-[:IS_METHOD_OF]->(method_parent:Class)
        OPTIONAL MATCH (n)-[:IS_ATTRIBUTE_OF]->(attr_parent:Class)
        OPTIONAL MATCH (n)-[:BELONGS_TO_DICT]->(dict:Dictionary)
        RETURN 
            n.name AS id,
            head(labels(n)) AS type,
            n.value AS value,     
            enum.name AS parent_enum,
            coalesce(method_parent.name, attr_parent.name, class.name, class2.name) AS parent_class,
            dict.name AS parent_dict,
            n.description AS description
        """
        record = session.run(cypher, entity_id=entity_id).single()
        return {
            "id": record["id"],
            "type": record["type"],
            "value": record.get("value"),
            "parent_enum": record["parent_enum"],
            "parent_class": record["parent_class"],
            "parent_dict": record["parent_dict"],
            "description": record["description"]
        } if record else None

    
    def _extract_keywords_with_parens_and_lexicon(self, query: str, language: str) -> list:
        words = re.findall(r'\b\w+\b', query.lower())
        keywords = []
        for w in words:
            en_w = FR_TO_EN_LEXICON.get(w, w) if language.lower().startswith("fr") else w
            if len(en_w) > 2:
                keywords.append(en_w)

        for paren_content in re.findall(r'\((.*?)\)', query):
            paren_content = paren_content.strip()
            if paren_content and paren_content not in keywords:
                keywords.append(paren_content)  
            motif = f"({paren_content})"
            if motif not in keywords:
                keywords.append(motif)
            for part in re.split(r'[,\s]+', paren_content):
                part = part.strip().lower()
                en_part = FR_TO_EN_LEXICON.get(part, part) if language.lower().startswith("fr") else part
                if len(en_part) > 2 and en_part not in keywords:
                    keywords.append(en_part)
        # print(f"[DEBUG] Keywords after preprocess (parens enrichies): {keywords}")
        return keywords



    def _find_best_dict_entities(self, session, dict_name, keywords, focus_ids, query, min_score=1):
        # print(f"\n=== [DEBUG] _find_best_dict_entities called for dict_name: {dict_name} ===")
        # print(f"    - Keywords: {keywords}")
        # print(f"    - focus_ids: {focus_ids}")
        # print(f"    - Query: {query}")
        if dict_name == "PtracReactionDict":
            cypher = """
            MATCH (d:Dictionary {name: $dict_name})<-[:BELONGS_TO_DICT]-(mt)
            RETURN mt.name AS id, mt.description AS desc
            """
            query_lower = query.lower()
            focus_particles = {p for p in PARTICLE_NAMES if p in query_lower}
            query_mt_numbers = extract_mt_numbers_from_query(query)
            query_keywords = set(re.findall(r'\w+', query_lower))
            reaction_patterns_in_query = extract_reaction_patterns_from_query(query)  

            # print(f"[DEBUG] Patterns (n,x) détectés dans query : {reaction_patterns_in_query}")

            all_mt = []
            max_score = 0
            for record in session.run(cypher, dict_name=dict_name):
                mt_entity = {
                    "id": record["id"],
                    "label": "",
                    "desc": record.get("desc") or "",
                }
                score = score_mt_entity(mt_entity, query_keywords, focus_particles, query_mt_numbers, reaction_patterns_in_query)
                mt_entity["score"] = score
                if score > max_score:
                    max_score = score
                all_mt.append(mt_entity)
                # print(f"[DEBUG MT] {mt_entity['id']}: score={score}, desc='{mt_entity['desc']}'")

            mt_sorted = sorted([ent for ent in all_mt if ent["score"] > 0], key=lambda e: -e["score"])
            # print("[DEBUG] MT triés par score :", [(e["id"], e["score"]) for e in mt_sorted])

            shortlist = []
            if mt_sorted:
                n_best = min(3, len(mt_sorted))
                third_score = mt_sorted[n_best - 1]["score"]
                for ent in mt_sorted:
                    if ent["score"] >= third_score:
                        shortlist.append(ent)
                    else:
                        break
                # print(f"[DEBUG] Shortlist (top 3 + ex aequo) : {[e['id'] for e in shortlist]}")

            results = []
            for ent in shortlist:
                full_ent = self.get_entity_full_info(session, ent["id"])
                if full_ent:
                    full_ent["score"] = ent["score"]
                    results.append(full_ent)
            return results

        if dict_name == "ParticleCodeDict":
            cypher = """
            MATCH (d:Dictionary {name: $dict_name})<-[:BELONGS_TO_DICT]-(p)
            RETURN p.name AS id, p.description AS desc
            """
            exclude_words = {"particle", "particles", "particule", "particules"}

            normalized_keywords = set(normalize(kw.rstrip('s')) for kw in keywords)
            normalized_keywords = {kw for kw in normalized_keywords if kw not in exclude_words}

            results = []
            debug_particle_scores = []
            for record in session.run(cypher, dict_name=dict_name):
                id = record.get("id", "")
                desc = record.get("desc") or ""
                desc_tokens = set(re.findall(r'\b\w+\b', desc.lower()))
                matched = False
                score = 0
                matched_kw = []
                for kw in normalized_keywords:
                    if kw in desc_tokens:
                        matched = True
                        score += 1
                        matched_kw.append(kw)
                debug_particle_scores.append(f"{id} (score={score}, kw={matched_kw}, desc={desc_tokens})")
                if matched:
                    full_ent = self.get_entity_full_info(session, id)
                    if full_ent:
                        full_ent["score"] = score
                        results.append(full_ent)
            # print("[DEBUG] PARTICLE_* scores :")
            for entry in debug_particle_scores:
                continue
                #print(f"    {entry}")
            shortlist_str = ", ".join(f"{e['id']} (score={e['score']})" for e in results)
            # print(f"SHORTLISTED (ParticleCodeDict): [{shortlist_str}]")

            specific_particles = set(normalize(p) for p in PARTICLE_NAMES if p != "particle")
            if results and len(results) > 1:
                if not (specific_particles & normalized_keywords):
                    # print("[DEBUG] Aucun nom de particule spécifique trouvé dans la requête (que 'particle'), on ne retourne aucun PARTICLE_X au LLM.")
                    return []

            return results
        
        if dict_name == "PtracZAIDDict":
            # print("=== [DEBUG] Entering PtracZAIDDict block ===")
            cypher = """
            MATCH (d:Dictionary {name: $dict_name})<-[:BELONGS_TO_DICT]-(z)
            RETURN z.name AS id, z.value AS value, z.description AS desc, z.symbol AS symbol
            """
            isotope_tokens = re.findall(r'[A-Za-z]{1,3}-\d{1,3}|\d{1,3}-[A-Za-z]{1,3}', query)

            zaid_keywords_raw = [
                kw for kw in keywords
                if re.match(r'^(?:[A-Za-z]{1,3}-?\d{1,3}|\d{1,3}-?[A-Za-z]{1,3}|\d{4,5})$', kw, re.IGNORECASE)
            ]
            zaid_keywords_raw += [kw for kw in isotope_tokens if kw not in zaid_keywords_raw]
            normalized_keywords = set()
            for kw in zaid_keywords_raw:
                norm = normalize(kw)
                normalized_keywords.add(norm)
                if '-' in kw:
                    normalized_keywords.add(norm.replace('-', ''))
                    normalized_keywords.add(kw.replace('-', '').lower())

            # print(f"[DEBUG] All keywords: {keywords}")
            # print(f"[DEBUG] ZAID-like keywords: {zaid_keywords_raw}")
            # print(f"[DEBUG] Normalized ZAID keywords (after tiret merge): {normalized_keywords}")

            results = []
            max_match = 0
            scored_matches = []
            strict_matched_ids = set()
            for record in session.run(cypher, dict_name=dict_name):
                id = record.get("id", "")
                value = str(record.get("value") or "")
                desc = str(record.get("desc") or "")
                symbol = str(record.get("symbol") or "")
                a, elem = "", ""
                m = re.match(r"NUCLIDE_?([0-9]+)([A-Z][a-z]?|)", id)
                if m:
                    a, elem = m.group(1), m.group(2)
                elif symbol:
                    elem = symbol
                canon_variants = set()
                if elem and a:
                    for variant in [
                        f"{elem}{a}", f"{a}{elem}", f"{elem}-{a}", f"{a}-{elem}",
                        f"{elem.lower()}{a}", f"{a}{elem.lower()}", f"{elem.lower()}-{a}", f"{a}-{elem.lower()}",
                        f"{elem.upper()}{a}", f"{a}{elem.upper()}", f"{elem.upper()}-{a}", f"{a}-{elem.upper()}",
                        f"{elem.capitalize()}{a}", f"{a}{elem.capitalize()}", f"{elem.capitalize()}-{a}", f"{a}-{elem.capitalize()}"
                    ]:
                        canon_variants.add(normalize(variant))
                canon_variants.add(normalize(value))
                canon_variants.add(normalize(id))
                canon_variants.add(normalize(symbol))
                canon_variants.add(normalize(desc))

                if desc:
                    match = re.search(r"([A-Z][a-z]+)[ -]?([0-9]+)", desc)
                    if match:
                        el_name, mass = match.groups()
                        canon_variants.update({
                            normalize(f"{el_name}{mass}"),
                            normalize(f"{mass}{el_name}"),
                            normalize(f"{el_name}-{mass}"),
                            normalize(f"{mass}-{el_name}"),
                            normalize(f"{el_name.lower()}{mass}"),
                            normalize(f"{mass}{el_name.lower()}"),
                            normalize(f"{el_name.lower()}-{mass}"),
                            normalize(f"{mass}-{el_name.lower()}"),
                        })
                # print(f"[DEBUG] ZAID RECORD: id={id}, value={value}, desc={desc}, symbol={symbol}")
                # print(f"[DEBUG] Canonical variants for {id}: {canon_variants}")

                match_count = 0
                strict_this_record = False
                for kw in normalized_keywords:
                    for variant in canon_variants:
                        if kw == variant:
                            # print(f"[DEBUG STRICT MATCH] kw='{kw}' == variant='{variant}' id={id}")
                            match_count += 2  # bonus
                            strict_this_record = True
                        elif kw in variant or variant in kw:
                            # print(f"[DEBUG SUBSTR MATCH] kw='{kw}' <-> variant='{variant}' id={id}")
                            match_count += 1
                if match_count:
                    # print(f"[KG ZAID MATCH] match_count={match_count}, id={id}, keywords={normalized_keywords & canon_variants}")
                    scored_matches.append((match_count, id))
                    if match_count > max_match:
                        max_match = match_count
                    if strict_this_record:
                        strict_matched_ids.add(id)

            if strict_matched_ids:
                # print(f"[DEBUG] All strict matches: {strict_matched_ids}")
                shortlisted = strict_matched_ids
            else:
                shortlisted = {id for (count, id) in scored_matches if count == max_match and max_match > 0}

            results = []
            for id in shortlisted:
                full_ent = self.get_entity_full_info(session, id)
                if full_ent:
                    results.append(full_ent)
            # print(f"SHORTLISTED (PtracZAIDDict): {shortlisted}")
            return results

    def find_best_enum_entities(self, session, prefix, keywords, focus_ids, query, bonus=False, bonus_label=None):
        #  print(f"\n=== [DEBUG] find_best_enum_entities called for {prefix} ===")
        #  print(f"    - keywords: {keywords}")
        #  print(f"    - focus_ids: {focus_ids}")
        #  print(f"    - bonus: {bonus} ({bonus_label})")
        #  print(f"    - query: {query}")

        cypher = f"MATCH (e) WHERE e.name STARTS WITH '{prefix}_' RETURN e.name AS id, e.description AS desc"
        scored_matches = []

        normalized_keywords = set()
        for kw in keywords:
            normalized_keywords.add(kw.lower())
            if kw.endswith('s') and len(kw) > 3:
                normalized_keywords.add(kw[:-1].lower())

        for record in session.run(cypher):
            entity_id = record.get("id", "")
            desc = record.get("desc", "") or ""
            id_norm = entity_id.lower()
            desc_norm = desc.lower()
            score = 0
            score_details = []
            for kw in normalized_keywords:
                if kw and kw in id_norm:
                    score += 6
                    score_details.append(f"ID~{kw}:+6")
            desc_tokens = set([w.strip('.,;:!?()[]{}') for w in desc_norm.split()])
            for kw in normalized_keywords:
                if kw in desc_tokens:
                    score += 7
                    score_details.append(f"DESC~{kw}:+7")
                if "(" in kw and kw in desc_norm:
                    score += 7
                    score_details.append(f"DESC~{kw}:+7")
            if bonus:
                score += 4
                score_details.append(f"BONUS_{bonus_label.upper()}:+4")
            # print(f"    - {entity_id}: score={score} [{', '.join(score_details) or '  '}] [desc='{desc}']")
            scored_matches.append((score, entity_id, score_details))

        scored_matches = [x for x in scored_matches if x[0] > 0]
        if not scored_matches:
            # print(f"SHORTLISTED ({prefix}): []")
            return []
        scored_matches.sort(reverse=True, key=lambda x: x[0])

        top_ids = []
        last_score = None
        for i, (score, entity_id, _) in enumerate(scored_matches):
            if i < 3:
                top_ids.append((entity_id, score))
                last_score = score
            elif score == last_score:
                top_ids.append((entity_id, score))
            else:
                break

        # Print shortlist triée
        # print(f"SHORTLISTED ({prefix}):", [f"{id} (score={score})" for id, score in top_ids])

        results = []
        for entity_id, _ in top_ids:
            full_ent = self.get_entity_full_info(session, entity_id)
            if full_ent:
                results.append(full_ent)
        return results


    def extract_kg_context(self, quiet_output: Dict[str, Any]) -> Dict[str, Any]:
        query = quiet_output.get("query", "")
        language = quiet_output.get("language", "en")
        focus_map = {
            k: quiet_output.get(k, [])
            for k in ["focus_events", "focus_data", "focus_dictionaries", "focus_classes", "focus_methods", "focus_attributes"]
        }
        focus_ids = {v.lower() for values in focus_map.values() for v in values if v}
        keywords = self._extract_keywords_with_parens_and_lexicon(query, language)
        # print(f"[DEBUG] Keywords after preprocess: {keywords}")

        entities, entities_seen = [], set()
        with self.driver.session() as session:
            candidate_ids = {}
            for focus_type in ["focus_data", "focus_classes", "focus_methods", "focus_attributes"]:
                for val in focus_map.get(focus_type, []):
                    if not val: continue
                    cypher = "MATCH (n) WHERE toUpper(n.name) = $focus RETURN n.name AS id"
                    result = session.run(cypher, focus=val.upper())
                    for record in result:
                        if record["id"]:
                            candidate_ids.setdefault(record["id"], set()).add(focus_type)
                            # print(f"[DEBUG] {focus_type} matched: {record['id']}")

            for dict_name in FOCUS_DICTIONARIES:
                if dict_name in focus_map["focus_dictionaries"]:
                    best_dict_entities = self._find_best_dict_entities(session, dict_name, keywords, focus_ids, query)
                    for ent in best_dict_entities:
                        if ent["id"] not in entities_seen:
                            ent["focus_type"] = ["dict_pruning"]
                            entities.append(ent)
                            entities_seen.add(ent["id"])

            focus_events = focus_map.get("focus_events", [])
            bnk_bonus = "bnk" in [v.lower() for v in focus_events]
            best_bnk_entities = self.find_best_enum_entities(
                session, prefix="BNK", keywords=keywords, focus_ids=focus_ids,
                query=query, bonus=bnk_bonus, bonus_label="BNK"
            )
            for ent in best_bnk_entities:
                if ent["id"] not in entities_seen:
                    ent["focus_type"] = ["bnk_focus"]
                    entities.append(ent)
                    entities_seen.add(ent["id"])

            ter_bonus = "ter" in [v.lower() for v in focus_events]
            best_ter_entities = self.find_best_enum_entities(
                session, prefix="TER", keywords=keywords, focus_ids=focus_ids,
                query=query, bonus=ter_bonus, bonus_label="TER"
            )
            for ent in best_ter_entities:
                if ent["id"] not in entities_seen:
                    ent["focus_type"] = ["ter_focus"]
                    entities.append(ent)
                    entities_seen.add(ent["id"])

            event_roots = ["TER", "BNK", "COL", "SRC", "SUR", "LST"]
            focus_events = [e.upper() for e in focus_map.get("focus_events", [])]

            for ev in event_roots:
                racine_ajoutee = False
                if ev in focus_events:
                    cypher = """
                    MATCH (n) WHERE n.name = $ev 
                    RETURN n.name AS id, n.description AS desc, n.value AS value, labels(n) AS labels
                    """
                    record = session.run(cypher, ev=ev).single()
                    if record and record["id"] not in entities_seen:
                        entity_info = {
                            "id": record["id"],
                            "type": record["labels"][0] if record["labels"] else None,
                            "parent_enum": None,
                            "parent_class": None,
                            "parent_dict": None,
                            "description": record["desc"],
                            "value": record.get("value"),
                            "focus_type": ["event_root"]
                        }
                        entities.append(entity_info)
                        entities_seen.add(record["id"])
                        racine_ajoutee = True
                        # print(f"[DEBUG] Ajout automatique event root explicite : {ev}")
                if not racine_ajoutee:
                    has_child = any(ent["id"].startswith(ev + "_") for ent in entities)
                    already_root = any(ent["id"] == ev for ent in entities)
                    if has_child and not already_root:
                        cypher = """
                        MATCH (n) WHERE n.name = $ev 
                        RETURN n.name AS id, n.description AS desc, n.value AS value, labels(n) AS labels
                        """
                        record = session.run(cypher, ev=ev).single()
                        if record and record["id"] not in entities_seen:
                            entity_info = {
                                "id": record["id"],
                                "type": record["labels"][0] if record["labels"] else None,
                                "parent_enum": None,
                                "parent_class": None,
                                "parent_dict": None,
                                "description": record["desc"],
                                "value": record.get("value"),
                                "focus_type": ["event_root_auto"]
                            }
                            entities.append(entity_info)
                            entities_seen.add(record["id"])
                            # print(f"[DEBUG] Ajout automatique event root IMPLICITE car enfant shortlisté : {ev}")

            for entity_id, sources in candidate_ids.items():
                if entity_id in entities_seen:
                    continue
                entity_info = self.get_entity_full_info(session, entity_id)
                if entity_info:
                    if entity_info.get("parent_dict") in focus_map["focus_dictionaries"]:
                        continue  # On ne réajoute pas les entités déjà shortlistées par dict pruning !
                    entity_info["focus_type"] = list(sources)
                    entities.append(entity_info)
                    entities_seen.add(entity_id)

        # print(f"[DEBUG] === FINAL KG CONTEXT ===")
        for ent in entities:
            # print(f"    - {ent['id']} ({ent.get('focus_type', '')})")

            return {
                "query": query,
                "focus_map": focus_map,
                "entities": entities,
            }

if __name__ == "__main__":
    emma = EMMA(neo4j_user="neo4j", neo4j_password="decima123")
    quiet = QUIET()
    test_query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Quelle est la position x, y, z et l'énergie et le temps des évènements de collisions"
    qout = quiet.analyze(test_query)
    kg_context = emma.extract_kg_context(qout)
    # print_llm_context(kg_context)
    emma.close()

