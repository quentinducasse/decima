# ajouter getPARTICULE à chaque evenement (donner dictionnaire PAR_)
# ajouter getRXN à chaque evenement (donner dictionnaire MT_)
import os
from mcnptools import Ptrac
from collections import OrderedDict, Counter

# === ENUMS cohérents avec PtracEnums.hpp ===
event_base_labels = {
    1000: "SRC", 2000: "BNK", 3000: "SUR", 4000: "COL", 5000: "TER", 9000: "LST"
}

bank_subtype_labels = {
    1: "BNK_DXT_TRACK", 2: "BNK_ERG_TME_SPLIT", 3: "BNK_WWS_SPLIT", 4: "BNK_WWC_SPLIT",
    5: "BNK_UNC_TRACK", 6: "BNK_IMP_SPLIT", 7: "BNK_N_XN_F", 8: "BNK_N_XG", 9: "BNK_FLUORESCENCE",
    10: "BNK_ANNIHILATION", 11: "BNK_PHOTO_ELECTRON", 12: "BNK_COMPT_ELECTRON", 13: "BNK_PAIR_ELECTRON",
    14: "BNK_AUGER_ELECTRON", 15: "BNK_PAIR_POSITRON", 16: "BNK_BREMSSTRAHLUNG", 17: "BNK_KNOCK_ON",
    18: "BNK_K_X_RAY", 19: "BNK_N_XG_MG", 20: "BNK_N_XF_MG", 21: "BNK_N_XN_MG", 22: "BNK_G_XG_MG",
    23: "BNK_ADJ_SPLIT", 24: "BNK_WWT_SPLIT", 25: "BNK_PHOTONUCLEAR", 26: "BNK_DECAY",
    27: "BNK_NUCLEAR_INT", 28: "BNK_RECOIL", 29: "BNK_DXTRAN_ANNIHIL", 30: "BNK_N_CHARGED_PART",
    31: "BNK_H_CHARGED_PART", 32: "BNK_N_TO_TABULAR", 33: "BNK_MODEL_UPDAT1", 34: "BNK_MODEL_UPDATE",
    35: "BNK_DELAYED_NEUTRON", 36: "BNK_DELAYED_PHOTON", 37: "BNK_DELAYED_BETA",
    38: "BNK_DELAYED_ALPHA", 39: "BNK_DELAYED_POSITRN"
}

termination_subtype_labels = {
    1: "TER_ESCAPE", 2: "TER_ENERGY_CUTOFF", 3: "TER_TIME_CUTOFF", 4: "TER_WEIGHT_WINDOW",
    5: "TER_CELL_IMPORTANCE", 6: "TER_WEIGHT_CUTOFF", 7: "TER_ENERGY_IMPORTANCE",
    8: "TER_DXTRAN", 9: "TER_FORCED_COLLISION", 10: "TER_EXPONENTIAL_TRANSFORM",
    # Grouped/shared values:
    11: "TER_GENCHAR_MULTIPLE_SCATTER / SCATTER / N_DOWNSCATTERING / P_COMPTON_SCATTER",
    12: "TER_GENCHAR_BREMSSTRAHLUNG / E_BREMSSTRAHLUNG / N_CAPTURE / P_CAPTURE",
    13: "TER_GENCHAR_NUCLEAR_INTERACTION / DECAY / N_N_XN / P_PAIR_PRODUCTION / E_INTERACTION_DECAY",
    14: "TER_GENCHAR_ELASTIC_SCATTER / N_FISSION / P_PHOTONUCLEAR",
    15: "TER_GENCHAR_DECAY / N_NUCLEAR_INTERACTION",
    16: "TER_GENCHAR_CAPTURE / N_PARTICLE_DECAY",
    17: "TER_GENCHAR_TABULAR_SAMPLING / N_TABULAR_BOUNDARY"
}

particle_labels = {
    1: "NEUTRON",         
    2: "PHOTON",          
    3: "ELECTRON",
    4: "POSITRON",
    5: "PROTON",
    6: "DEUTERON",
    7: "TRITON",
    8: "HELIUM3",
    9: "ALPHA",
    10: "HEAVY_ION",
    11: "CHARGED",
    12: "NEUTRAL"
}

ptrac_data_fields = OrderedDict([
    (1, "NPS"), (2, "FIRST_EVENT_TYPE"), (3, "NPSCELL"), (4, "NPSSURFACE"),
    (5, "TALLY"), (6, "VALUE"), (7, "NEXT_EVENT_TYPE"), (8, "NODE"), (9, "NSR"),
    (10, "ZAID"), (11, "RXN"), (12, "SURFACE"), (13, "ANGLE"), (14, "TERMINATION_TYPE"),
    (15, "BRANCH"), (16, "PARTICLE"), (17, "CELL"), (18, "MATERIAL"),
    (19, "COLLISION_NUMBER"), (20, "X"), (21, "Y"), (22, "Z"),
    (23, "U"), (24, "V"), (25, "W"), (26, "ENERGY"), (27, "WEIGHT"),
    (28, "TIME"), (29, "SOURCE_TYPE"), (30, "BANK_TYPE")
])

# === Script principal ===
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/example_ptrac_1.mcnp_extended_ascii.ptrac"))
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/example_ptrac_1.mcnp_extended_thermal.ptrac"))
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/example_ptrac_1.mcnp_extended_14MeV_modeNP.ptrac"))
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/example_ptrac_1.mcnp_extended_14MeV_modeNPE.ptrac"))
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_ASCII.ptrac"))
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_20mb_ASCII.ptrac"))
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_82mb_ASCII.ptrac")) #### marche pas !
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_tally8_ASCII.ptrac")) #### marche pas !
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_event_src_col_ASCII.ptrac"))  #### marche pas !
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_event_src_col_BIN.ptrac"))  #### FONCTIONNE !!!
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_7mb_BIN.ptrac")) 
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_70mb_BIN.ptrac")) 
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ptrac_samples/LB6411_cezane_SC_75_tally8_BIN.ptrac"))  #### FONCTIONNE !!!


print("=== DÉMARRAGE DU SCRIPT ===")
print(f"[DEBUG] Chargement fichier : {file_path}")

ptrac = Ptrac(file_path, Ptrac.ASC_PTRAC)
# ptrac = Ptrac(file_path, Ptrac.BIN_PTRAC)

print(f"AVANT ReadHistories")
histories = ptrac.ReadHistories(1)
print(f"APRES ReadHistories")

summary = {
    "total_histories": 0,
    "total_events": 0,
    "total_BNK": 0,
    "total_TER": 0,
    "bank_types": Counter(),
    "termination_types": Counter(),
    "particle_types": Counter()
}

for i, hist in enumerate(histories):
    summary["total_histories"] += 1
    print(f"\n========== HISTOIRE #{i+1} ==========")
    print(f"Nombre d’événements : {hist.GetNumEvents()}")
    summary["total_events"] += hist.GetNumEvents()

    for j in range(hist.GetNumEvents()):
        evt = hist.GetEvent(j)
        evt_type = evt.Type()
        base_code = (evt_type // 1000) * 1000
        base_label = event_base_labels.get(base_code, f"UNKNOWN({evt_type})")

        print(f"\n  ➤ Événement #{j+1} : {base_label} (type {evt_type})")

        if base_label == "BNK":
            summary["total_BNK"] += 1
            try:
                code = evt.BankType()
                subtype_label = bank_subtype_labels.get(code, f"UNKNOWN_BNK({code})")
                summary["bank_types"][code] += 1
                print(f"    → BANK_TYPE = {code} ({subtype_label})")
            except Exception as e:
                print(f"    → BANK_TYPE non accessible : {e}")

        elif base_label == "TER":
            summary["total_TER"] += 1
            try:
                if evt.Has(14):
                    code = int(evt.Get(14))
                    subtype_label = termination_subtype_labels.get(code, f"UNKNOWN_TER({code})")
                    summary["termination_types"][code] += 1
                    print(f"    → TERMINATION_TYPE = {code} ({subtype_label})")
            except Exception as e:
                print(f"    → TERMINATION_TYPE non accessible : {e}")

        if evt.Has(16):
            try:
                code = int(evt.Get(16))
                label = particle_labels.get(code, f"UNKNOWN_PARTICLE({code})")
                summary["particle_types"][code] += 1
                print(f"    → PARTICLE = {code} ({label})")
            except Exception as e:
                print(f"    → PARTICLE non accessible : {e}")

        for field_code, field_label in ptrac_data_fields.items():
            if evt.Has(field_code):
                try:
                    val = evt.Get(field_code)
                    print(f"    - {field_label:20s} = {val}")
                except Exception as e:
                    print(f"    - {field_label:20s} = [ERREUR: {e}]")

# === RÉCAPITULATIF GLOBAL ===
print("\n=== RÉCAPITULATIF GLOBAL ===")
print(f"Nombre total d’histoires analysées : {summary['total_histories']}")
print(f"Nombre total d’événements : {summary['total_events']}")
print(f"Nombre total d’événements BNK : {summary['total_BNK']}")
print(f"Nombre total d’événements TER : {summary['total_TER']}")

print("\n→ Répartition des BANK_TYPE rencontrés :")
for code, count in summary["bank_types"].most_common():
    label = bank_subtype_labels.get(code, f"UNKNOWN_BNK({code})")
    print(f"  BANK_TYPE = {code:2d} ({label}) : {count} occurrence(s)")

print("\n→ Répartition des TERMINATION_TYPE rencontrés :")
for code, count in summary["termination_types"].most_common():
    label = termination_subtype_labels.get(code, f"UNKNOWN_TER({code})")
    print(f"  TERMINATION_TYPE = {code:2d} ({label}) : {count} occurrence(s)")

print("\n→ Répartition des PARTICULES rencontrées :")
for code, count in summary["particle_types"].most_common():
    label = particle_labels.get(code, f"UNKNOWN_PARTICLE({code})")
    print(f"  PARTICLE = {code:2d} ({label}) : {count} occurrence(s)")
