# utils/keywords_quiet.py

# ==============================
# FOCUS_EVENTS —  PTRAC events
# ==============================

FOCUS_EVENTS = {
    "SRC": [
        "source", "source event", "sources","évènements sources", "source particle", "neutron source", "particule source", "particules sources",
        "initiation", "emission", "émission", "start", "départ"
    ],
    "BNK": [
        "bank", "bank event", "banque", "évènement banque", "banked", "banques", "importance splitting", "split", "splitting",
        "multiplied", "multipliée", "multipliées", "multiplié", "clone", "cloné", "clonés", "cloned neutrons",
        "particule clonée", "particules secondaires", "générées", "générés", "générée", "généré",
        "particule secondaire", "secondary particle", "secondary particles", "secondaries", "particules créées", "created particles", "generated particles",
        "AAZZZ", "ZAID", "interact", "interaction", "interactions", "interaction d'importance"
    ],
    "COL": [
        "collision", "évènement collision", "collision event" "collisions", "interact", "interaction", "interactions", "impact", "impacts", "scattering", "diffusion",
        "heurte", "heurts", "choc", "chocs", "réaction", "réactions", "reaction", "reaction type", "types de réaction", "isotope", "isotopes",
        "AAZZZ", "ZAID"
    ],
    "TER": [
        "termination", "termination event", "terminaison",  "évènement terminaison" "terminent", "terminée", "fin", "finish", "die", "absorbed", "absorbee", "absorbe", "absorbé", "absorber", "absorption",
        "perte", "perdu", "perdus", "disparu", "disparue", "disparus",
        "captured", "capture", "captures", "capturé", "capturés", "capturées",
        "stop", "stopping", "cutoff", "cut-off", "threshold", "seuil", "escape", "escaped", "disappear", "fuite", "fuir", "out of bounds",
        "roulette", "russian roulette", "interrompu", "interruption"
    ],
    "SUR": [
        "surface", "surfaces", "surfaces évènements", "surface event" "boundary", "boundaries", "wall", "cross", "crossing", "interface",
        "traverse", "traversent", "traversée", "franchit", "franchissent"
    ],
    "LST": [
        "lost", "lost event", "vanished", "disappeared", "missing", "manquant", "absent", "inconnu", "perte", "perdu", "perdus", "perdues"
    ]
}

# ============================
# FOCUS_DATA — PTRAC
# ============================

FOCUS_DATA = {
    "NPS":              ["nps", "history number", "numéro d'histoire", "numéro de trajet"],
    "FIRST_EVENT_TYPE": ["first event type", "premier type d'événement", "début d'historique", "événement initial"],
    "NPSCELL":          ["npscell", "cellule nps", "cellule filtrage", "cellule d’histoire"],
    "NPSSURFACE":       ["npssurface", "surface nps", "surface filtrage", "surface d’histoire"],
    "TALLY":            ["tally", "détecteur", "compteur", "numéro de tally"],
    "VALUE":            ["value", "valeur", "score", "résultat"],
    "NEXT_EVENT_TYPE":  ["next event type","next event", "prochain événement", "événement suivant", "étape suivante"],
    "NODE":             ["node", "nœud", "noeud", "numéro de nœud"],
    "NSR":              ["nsr", "number of sub-runs", "sous-simulation", "numéro de run"],
    "ZAID":             ["zaid", "isotope", "nucléide", "noyau"],
    "RXN":              ["rxn", "reaction", "réaction", "réactions", "type de réaction", "scattering", "scattered", "diffusé", "diffusion", "diffusés", "diffusées"],
    "SURFACE":          ["surface", "surfaces", "numéro de surface", "frontière"],
    "ANGLE":            ["angle", "angles", "orientation", "direction angulaire"],
    "TERMINATION_TYPE": ["termination type", "type de terminaison", "raison d’arrêt", "mode d'arrêt"],
    "BRANCH":           ["branch", "maille", "branche", "univers"],
"PARTICLE": [
    "particle", "particles", "particule", "particules", "type de particule", "espèce", "espèces",
    "neutron", "neutrons",
    "photon", "photons",
    "électron", "electron", "électrons", "electrons",
    "positron", "positrons",
    "proton", "protons",
    "deuteron", "deutéron", "deutons", "deuterons",
    "triton", "tritons",
    "alpha", "alphas", "alpha particle", "particule alpha",
    "helium", "helium3", "helion", "hélium", "hélium3", "hélion",
    "heavy ion", "heavy ions", "ion lourd", "ions lourds",
    "charged particle", "charged particles", "particule chargée", "particules chargées",
    "neutral particle", "neutral particles", "particule neutre", "particules neutres"
],    
"CELL":             ["cell", "cells", "cellule", "cellules"],
    "MATERIAL":         ["material", "matériau", "matériaux", "numéro matériau"],
    "COLLISION_NUMBER": ["collision number", "nombre de collisions", "collisions", "numéro de collision"],
    "X":                ["x", "coordonnée x", "abscisse", "position x"],
    "Y":                ["y", "coordonnée y", "ordonnée", "position y"],
    "Z":                ["z", "coordonnée z", "altitude", "position z"],
    "U":                ["u", "direction u", "cosinus u", "vecteur u"],
    "V":                ["v", "direction v", "cosinus v", "vecteur v"],
    "W":                ["w", "direction w", "cosinus w", "vecteur w"],
    "ENERGY":           ["energy", "énergie", "energies", "énergies", "mev", "MeV", "GeV", "eV", "electronvolts"],
    "WEIGHT":           ["weight", "poids", "weights", "poids des particules"],
    "TIME":             ["time", "temps", "timing", "durée", "coincidence", "coincidences", "seconds", "ms", "µs", "ns"],
    "SOURCE_TYPE":      ["source type", "type de source", "origine source", "particule source"],
    "BANK_TYPE":        ["bank type", "type de banque", "origine banque", "identifiant banque"]
}

# ===============================================
# FOCUS_DICTIONARIES 
# ===============================================

FOCUS_DICTIONARIES = {
    "ParticleCodeDict": [
        "neutron", "neutrons", "proton", "protons", "photon", "photons",
        "électron", "electrons", "electron", "électrons", "positron", "positrons", "deuteron", "deutons", "triton", "tritons",
        "alpha", "alphas", "helium", "helium3", "helion", "hélium", "hélium3", "hélion", "ion", "ions", "heavy ion", "heavy ions",
        "particule", "particules", "particle", "particles", "charged particle", "neutral particle"
    ],
    "PtracZAIDDict": [
        # general keywords
        "zaid", "zzaaa", "isotope", "isotopes", "noyau", "noyaux", "nucléide", "nucléides",
        "element", "élément", "éléments", "atomic", "atomique", "nuclide", "nuclides",
        "radionuclide", "radionuclides", "radionucléide", "radionucléides",
        "mass number", "atomic number",
        # Symbols
        "hydrogen", "deuterium", "tritium", "helium", "lithium", "beryllium", "bore", "carbone", "carbone-12", "carbone-13", "carbon",
        "azote", "nitrogen", "oxygen", "oxygène", "fluor", "fluorine", "neon", "néon", "sodium", "magnésium", "aluminium",
        "silicon", "silicium", "phosphorus", "phosphore", "soufre", "sulfur", "chlore", "chlorine", "argon", "potassium", "calcium",
        "scandium", "titanium", "vanadium", "chrome", "chromium", "manganèse", "manganese", "fer", "iron", "cobalt", "nickel",
        "cuivre", "copper", "zinc", "argent", "silver", "or", "gold", "plomb", "lead", "mercure", "mercury", "étain", "tin",
        "uranium", "plutonium", "thorium", "neptunium", "americium", "curium",
        # Chemical Symbols 
        "H", "D", "T", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al",
        "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni",
        "Cu", "Zn", "Ag", "Au", "Pb", "Hg", "Sn", "U", "Pu", "Th", "Np", "Am", "Cm",
        # Common isotopes
        "235u", "u235", "u-235", "uranium-235", "238u", "u238", "u-238", "uranium-238",
        "63cu", "cu63", "cu-63", "copper-63", "64zn", "zn64", "zn-64", "zinc-64",
        "56fe", "fe56", "fe-56", "iron-56",
        "16o", "o16", "o-16", "oxygen-16",
        "14n", "n14", "n-14", "nitrogen-14",
        "2h", "h2", "d", "deuterium",
        "3h", "h3", "t", "tritium",
        "12c", "c12", "c-12", "carbon-12",
        "13c", "c13", "c-13", "carbon-13",
    ],
    "PtracReactionDict": [
        "reaction", "réaction", "réactions", "rxn", "mt", "reaction type", "type de réaction", "types de réaction", "capture", "absorption",
        "elastic", "elastique", "elastic scattering", "diffusion élastique", "inelastic", "inelastique", "inelastic scattering", "diffusion inélastique",
        "non-elastic", "non elastique", "section efficace", "cross section", "absorption", "fission", "scission"
    ]
}

# ================================
# FOCUS_CLASSES 
# ================================
FOCUS_CLASSES = {
    "Ptrac": [
        "ptrac class", "ptrac", "parser", "parsing", "parseur", "fichier ptrac", "fichier de trajectoires",
    ],
    "PtracEvent": [
        "event class", "event", "événement", "évènement", "événements", "évènements"
    ],
    "PtracHistory": [
        "class histoiry", "history", "histoire", "trajet", "trajet de particule", "historique", "trajectoire"
    ],
    "PtracNps": [
        "nps class", "classe nps", "histoire numéro", "number of histories", "number of particles", "numéro d'histoire", "nombre de histories"
    ],
    "PtracEnums": [
        "enum", "enum class", "énumération", "classe d'enum"
    ]
}

# ================================
# FOCUS_METHODS 
# ================================
FOCUS_METHODS = {
    "Type()": [
        "type method", "méthode type", "type d'événement", "type d'evenement"
    ],
    "BankType()": [
        "bank type", "type de banque", "type de bank", "méthode banktype", "banktype method"
    ],
    "Has(DATA)": [
        "has", "possède", "posseder", "contient", "contient le champ", "présence de"
    ],
    "Get(DATA)": [
        "get", "obtenir", "récupérer", "extraire", "valeur de", "donne la valeur"
    ],
    "GetNPS()": [
        "get nps", "numéro d'histoire", "numéro de trajet", "nombre de nps", "nombre de particules"
    ],
    "GetNumEvents()": [
        "get number of events", "nombre d'événements", "nombre d'evenements", "nombre d'events"
    ],
    "GetEvent(I)": [
        "get event", "récupérer l'événement", "récupérer l'evenement", "événement numéro", "evenement numéro"
    ],
    "NPS()": [
        "nps method", "nombre de particules méthode"
    ],
    "Cell()": [
        "cell method", "méthode cellule"
    ],
    "Surface()": [
        "surface method", "méthode surface"
    ],
    "Tally()": [
        "tally method", "méthode tally", "détecteur"
    ],
    "Value()": [
        "value", "valeur", "méthode value", "résultat", "score"
    ],
    "ReadHistories(NUM)": [
        "read histories", "lire les histoires", "charger les histoires", "charger les trajectoires"
    ],
    "ReadHistoriesLegacy(NUM)": [
        "read histories legacy"
    ],
    "ReadHistory()": [
        "read history", "lire une histoire", "lire la trajectoire"
    ],
    "ReadHeader()": [
        "read header", "lire l'en-tête", "entête", "header"
    ]
}

# ==================================
# FOCUS_ATTRIBUTES
# ==================================
FOCUS_ATTRIBUTES = {
    "m_type": [
        "type d'événement", "event type", "m_type"
    ],
    "m_data": [
        "data", "m_data", "valeurs de l'événement"
    ],
    "m_bnktype": [
        "bank type", "m_bnktype", "type de banque"
    ],
    "m_nps": [
        "nps", "m_nps", "nombre de particules filtre", "nombre de particules filter",
    ],
    "m_events": [
        "événements", "m_events", "evenements", "liste d'événements", "liste d'evenements"
    ],
    "m_cell": [
        "m_cell", "cellule de filtrage", "cellule filtre", "cell filter"
    ],
    "m_surface": [
        "m_surface", "surface de filtrage", "surface filtre", "surface filter"
    ],
    "m_tally": [
        "tally", "m_tally", "tally de filtrage", "tally filtre", "tally filter"
    ],
    "m_value": [
        "value", "m_value", "valeur", "score", "score tally"
    ]
}
