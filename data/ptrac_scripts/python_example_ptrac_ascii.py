from mcnptools import Ptrac
from collections import defaultdict
from sys import stdout

# === Définition des enums connus ===

ptrac_data_enums = {
    "NPS": Ptrac.NPS, "FIRST_EVENT_TYPE": Ptrac.FIRST_EVENT_TYPE,
    "NPSCELL": Ptrac.NPSCELL, "NPSSURFACE": Ptrac.NPSSURFACE,
    "TALLY": Ptrac.TALLY, "VALUE": Ptrac.VALUE,
    "NEXT_EVENT_TYPE": Ptrac.NEXT_EVENT_TYPE, "NODE": Ptrac.NODE,
    "NSR": Ptrac.NSR, "ZAID": Ptrac.ZAID, "RXN": Ptrac.RXN,
    "SURFACE": Ptrac.SURFACE, "ANGLE": Ptrac.ANGLE,
    "TERMINATION_TYPE": Ptrac.TERMINATION_TYPE, "BRANCH": Ptrac.BRANCH,
    "PARTICLE": Ptrac.PARTICLE, "CELL": Ptrac.CELL,
    "MATERIAL": Ptrac.MATERIAL, "COLLISION_NUMBER": Ptrac.COLLISION_NUMBER,
    "X": Ptrac.X, "Y": Ptrac.Y, "Z": Ptrac.Z,
    "U": Ptrac.U, "V": Ptrac.V, "W": Ptrac.W,
    "ENERGY": Ptrac.ENERGY, "WEIGHT": Ptrac.WEIGHT, "TIME": Ptrac.TIME,
    "SOURCE_TYPE": Ptrac.SOURCE_TYPE, "BANK_TYPE": Ptrac.BANK_TYPE,
}

ptrac_bank_type_values = {
    "BNK_DXT_TRACK": 1, "BNK_ERG_TME_SPLIT": 2, "BNK_WWS_SPLIT": 3, "BNK_WWC_SPLIT": 4,
    "BNK_UNC_TRACK": 5, "BNK_IMP_SPLIT": 6, "BNK_N_XN_F": 7, "BNK_N_XG": 8,
    "BNK_FLUORESCENCE": 9, "BNK_ANNIHILATION": 10, "BNK_PHOTO_ELECTRON": 11,
    "BNK_COMPT_ELECTRON": 12, "BNK_PAIR_ELECTRON": 13, "BNK_AUGER_ELECTRON": 14,
    "BNK_PAIR_POSITRON": 15, "BNK_BREMSSTRAHLUNG": 16, "BNK_KNOCK_ON": 17,
    "BNK_K_X_RAY": 18, "BNK_N_XG_MG": 19, "BNK_N_XF_MG": 20, "BNK_N_XN_MG": 21,
    "BNK_G_XG_MG": 22, "BNK_ADJ_SPLIT": 23, "BNK_WWT_SPLIT": 24, "BNK_PHOTONUCLEAR": 25,
    "BNK_DECAY": 26, "BNK_NUCLEAR_INT": 27, "BNK_RECOIL": 28, "BNK_DXTRAN_ANNIHIL": 29,
    "BNK_N_CHARGED_PART": 30, "BNK_H_CHARGED_PART": 31, "BNK_N_TO_TABULAR": 32,
    "BNK_MODEL_UPDAT1": 33, "BNK_MODEL_UPDATE": 34, "BNK_DELAYED_NEUTRON": 35,
    "BNK_DELAYED_PHOTON": 36, "BNK_DELAYED_BETA": 37, "BNK_DELAYED_ALPHA": 38,
    "BNK_DELAYED_POSITRN": 39,
}

ptrac_termination_values = {
    1: "TER_ESCAPE", 2: "TER_ENERGY_CUTOFF", 3: "TER_TIME_CUTOFF",
    4: "TER_WEIGHT_WINDOW", 5: "TER_CELL_IMPORTANCE", 6: "TER_WEIGHT_CUTOFF",
    7: "TER_ENERGY_IMPORTANCE", 8: "TER_DXTRAN", 9: "TER_FORCED_COLLISION",
    10: "TER_EXPONENTIAL_TRANSFORM", 11: "TER_*_SCATTER",
    12: "TER_*_CAPTURE / BREMS / ELASTIC", 13: "TER_*_FISSION / DECAY / INTERACTION",
    14: "TER_GENCHAR_ELASTIC_SCATTER", 15: "TER_GENCHAR_DECAY",
    16: "TER_GENCHAR_CAPTURE", 17: "TER_GENCHAR_TABULAR_SAMPLING",
}

event_labels = {
    Ptrac.SRC: "SRC", Ptrac.BNK: "BNK", Ptrac.SUR: "SUR",
    Ptrac.COL: "COL", Ptrac.TER: "TER", Ptrac.LST: "LST"
}

# === Init ===
data_presence = defaultdict(bool)
bank_type_found = set()
termination_values_found = set()
event_type_count = defaultdict(int)

# === Chargement PTRAC ASCII ===
p = Ptrac("..\\ptrac_samples\\example_ptrac_1.mcnp_extended_ascii.ptrac", Ptrac.ASC_PTRAC)
hists = p.ReadHistories(10000)

# === Loop principal ===
while hists:
    for h in hists:
        for e in range(h.GetNumEvents()):
            event = h.GetEvent(e)
            etype = event.Type()
            event_type_count[etype] += 1

            for label, code in ptrac_data_enums.items():
                if event.Has(code):
                    data_presence[label] = True

            if etype == Ptrac.BNK and event.Has(Ptrac.BANK_TYPE):
                bank_type_found.add(int(event.Get(Ptrac.BANK_TYPE)))

            if etype == Ptrac.TER and event.Has(Ptrac.TERMINATION_TYPE):
                termination_values_found.add(int(event.Get(Ptrac.TERMINATION_TYPE)))
    hists = p.ReadHistories(10000)

# === Résumé ===

print("\n=== Résumé : Champs présents dans les événements ===\n")
for label in sorted(ptrac_data_enums.keys()):
    print(f"{label:<20} : {'✅ Présent' if data_presence[label] else '❌ Absent'}")

print("\n=== Types BANK_TYPE rencontrés ===\n")
reverse_bank = {v: k for k, v in ptrac_bank_type_values.items()}
for b in sorted(bank_type_found):
    print(f"  - {b:2} : {reverse_bank.get(b, '❓ Inconnu')}")

print("\n=== Types TERMINATION_TYPE rencontrés ===\n")
for t in sorted(termination_values_found):
    print(f"  - {t:2} : {ptrac_termination_values.get(t, '❓ Inconnu')}")

print("\n=== Types d'événements rencontrés (PTRAC Event Types) ===\n")
for code in sorted(event_type_count.keys()):
    print(f"  - {event_labels.get(code, f'UNKNOWN({code})'):<4} : {event_type_count[code]}")
