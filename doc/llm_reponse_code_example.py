from mcnptools import Ptrac

# Chemin du fichier PTRAC
ptrac_path = '<PTRAC_PATH_PLACEHOLDER>'

# Initialiser le fichier PTRAC
ptrac = Ptrac(ptrac_path)

# Lire la première histoire
histories = ptrac.ReadHistories(1)
if not histories:
    raise ValueError("Aucune histoire trouvée dans le fichier PTRAC.")

# Extraire la première histoire
history = histories[0]

# Compteur pour les électrons
electron_count = 0

# Parcourir les événements de l'histoire
for i in range(history.GetNumEvents()):
    event = history.GetEvent(i)

    # Vérifier si l'événement est un SRC ou BNK et concerne un électron
    if (event.Type() == Ptrac.SRC or event.Type() == Ptrac.BNK) and event.Has(Ptrac.PARTICLE) and event.Get(Ptrac.PARTICLE) == 3:
        # Informations initiales
        if event.Has(Ptrac.X) and event.Has(Ptrac.Y) and event.Has(Ptrac.Z) and event.Has(Ptrac.ENERGY) and event.Has(Ptrac.TIME) and event.Has(Ptrac.CELL):
            x_init = event.Get(Ptrac.X)
            y_init = event.Get(Ptrac.Y)
            z_init = event.Get(Ptrac.Z)
            energy_init = event.Get(Ptrac.ENERGY)
            time_init = event.Get(Ptrac.TIME)
            cell_init = event.Get(Ptrac.CELL)

        # Parcourir jusqu'à l'événement TER correspondant
        for j in range(i + 1, history.GetNumEvents()):
            next_event = history.GetEvent(j)
            if next_event.Type() == Ptrac.TER:
                if next_event.Has(Ptrac.TIME) and next_event.Has(Ptrac.TERMINATION_TYPE):
                    time_final = next_event.Get(Ptrac.TIME)
                    termination_type = next_event.Get(Ptrac.TERMINATION_TYPE)
                    time_of_flight = time_final - time_init

                    # Afficher les informations
                    print(f"Electron {electron_count + 1}:")
                    print(f"  Position initiale: ({x_init}, {y_init}, {z_init})")
                    print(f"  Énergie initiale: {energy_init}")
                    print(f"  Temps de vol: {time_of_flight}")
                    print(f"  Cellule initiale: {cell_init}")
                    print(f"  Type de terminaison: {termination_type}")
                    print()

                    # Incrémenter le compteur d'électrons
                    electron_count += 1
                    break

        # Arrêter après avoir trouvé trois électrons
        if electron_count >= 3:
            break