from mcnptools import Ptrac
import numpy as np

# Ouvrir le fichier PTRAC en tant que fichier binaire
p = Ptrac(r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\example_ptrac_1.mcnp_ASCII.ptrac", Ptrac.ASC_PTRAC)

energies = []

# Lire les histoires par lots de 10000
hists = p.ReadHistories(10000)
while hists:
    # Parcourir toutes les histoires
    for h in hists:
        # Parcourir tous les événements dans l'histoire
        for e in range(h.GetNumEvents()):
            event = h.GetEvent(e)
            # Vérifier si l'événement est de type SUR et que la surface est 300
            if event.Type() == Ptrac.SUR and event.Get(Ptrac.SURFACE) == 300:
                # Ajouter l'énergie à la liste
                energies.append(event.Get(Ptrac.ENERGY))
    # Lire le prochain lot d'histoires
    hists = p.ReadHistories(10000)

# Calculer l'énergie moyenne
average_energy = np.mean(energies) if energies else 0
print(f"L'énergie moyenne des neutrons traversant la surface 300 est : {average_energy:.5e} MeV")