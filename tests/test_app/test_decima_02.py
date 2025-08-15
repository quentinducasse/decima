

from mcnptools import Ptrac

# Chemin du fichier PTRAC
ptrac_path = r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\example_ptrac_1.mcnp_extended_14MeV_modeNPE.ptrac"

# Ouvrir le fichier PTRAC
ptrac = Ptrac(ptrac_path, Ptrac.ASC_PTRAC)

# Initialiser les compteurs
escape_count = 0
bremsstrahlung_count = 0

# Lire les histoires par lots
histories = ptrac.ReadHistories(10000)
while histories:
    for history in histories:
        for event_index in range(history.GetNumEvents()):
            event = history.GetEvent(event_index)

            # Vérifier si l'événement est de type TER
            if event.Type() == Ptrac.TER:
                # Vérifier si la particule est un électron
                if event.Has(Ptrac.PARTICLE) and event.Get(Ptrac.PARTICLE) == 3:
                    # Vérifier le type de terminaison
                    if event.Has(Ptrac.TERMINATION_TYPE):
                        termination_type = event.Get(Ptrac.TERMINATION_TYPE)
                        if termination_type == Ptrac.TER_ESCAPE:
                            escape_count += 1
                        elif termination_type == Ptrac.TER_E_BREMSSTRAHLUNG:
                            bremsstrahlung_count += 1

    # Lire le prochain lot d'histoires
    histories = ptrac.ReadHistories(10000)

# Afficher les résultats
print(f"Nombre d'électrons disparaissant par escape: {escape_count}")
print(f"Nombre d'électrons disparaissant par bremsstrahlung: {bremsstrahlung_count}")
