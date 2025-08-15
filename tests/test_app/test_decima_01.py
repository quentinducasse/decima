# existe-t-il des électrons qui terminent bremstrahlung et si oui print leur énergie, sinon print l'énergie moyenne de tous les electrons 

from mcnptools import Ptrac
from sys import stdout

# Chemin du fichier PTRAC
ptrac_path = r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\example_ptrac_1.mcnp_extended_14MeV_modeNPE.ptrac"

# Ouvrir le fichier PTRAC en tant que fichier binaire
p = Ptrac(ptrac_path, Ptrac.ASC_PTRAC)

# Initialiser les variables pour le comptage et la somme des énergies
electron_bremstrahlung_energies = []
total_energy = 0.0
electron_count = 0

# Lire les histoires par lots de 10000
hists = p.ReadHistories(10000)
while hists:
    # Boucler sur toutes les histoires
    for h in hists:
        # Boucler sur tous les événements dans l'histoire
        for e in range(h.GetNumEvents()):
            event = h.GetEvent(e)

            # Vérifier si l'événement est une terminaison d'électron par bremstrahlung
            if event.Type() == Ptrac.TER and event.Has(Ptrac.PARTICLE) and event.Get(Ptrac.PARTICLE) == 3:
                print("⚡ Électron trouvé avec événement TER")
                # if event.Has(Ptrac.TERMINATION_TYPE) and event.Get(Ptrac.TERMINATION_TYPE) == Ptrac.TER_E_BREMSSTRAHLUNG:
                if event.Has(Ptrac.TERMINATION_TYPE) and event.Get(Ptrac.TERMINATION_TYPE) == Ptrac.TER_ENERGY_CUTOFF: # raouter par moi-meme (pas par le LLM)
                    energy = event.Get(Ptrac.ENERGY)
                    electron_bremstrahlung_energies.append(energy)
                    print(f"☢️  Électron terminé par energy cuttoff — énergie : {energy:.5e} MeV")
                # Accumuler l'énergie pour tous les électrons
                total_energy += event.Get(Ptrac.ENERGY)
                electron_count += 1
                print(f"➕ Énergie ajoutée au total — énergie : {total_energy:.5e} MeV")

    hists = p.ReadHistories(10000)

# Vérifier et imprimer les résultats
if electron_bremstrahlung_energies:
    stdout.write("Énergies des électrons terminant par bremstrahlung:\n")
    for energy in electron_bremstrahlung_energies:
        stdout.write(f"{energy:.5e}\n")
else:
    if electron_count > 0:
        average_energy = total_energy / electron_count
        stdout.write(f"Énergie moyenne de tous les électrons: {average_energy:.5e}\n")
    else:
        stdout.write("Aucun électron trouvé.\n")