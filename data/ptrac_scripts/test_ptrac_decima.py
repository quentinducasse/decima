from mcnptools import Ptrac

# Chemin du fichier PTRAC
p = Ptrac(r"C:\Users\qduca\OneDrive\Applications\DECIMA_v2\data\ptrac_samples\example_ptrac_1.mcnp_extended_14MeV_modeNPE.ptrac", Ptrac.ASC_PTRAC)



# Lire les 1000 premières histoires
hists = p.ReadHistories(1000)

# Parcourir chaque histoire
for h in hists:
    # Parcourir chaque événement dans l'histoire
    for e in range(h.GetNumEvents()):
        event = h.GetEvent(e)
        
        # Vérifier si l'événement est de type TER (termination)
        if event.Type() == Ptrac.TER:
            # Vérifier si la terminaison est TER_E_BREMSSTRAHLUNG
            if event.Get(Ptrac.TERMINATION_TYPE) == Ptrac.TER_E_BREMSSTRAHLUNG:
                # Vérifier si la particule est un électron (code 3)
                if event.Get(Ptrac.PARTICLE) == 3:
                    # Extraire et afficher l'énergie de l'électron
                    energy = event.Get(Ptrac.ENERGY)
                    print(f"Électron avec terminaison bremstrahlung trouvé, énergie: {energy:.5e} MeV")