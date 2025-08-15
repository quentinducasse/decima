KG_CONTEXT_RULES = """

RÈGLES ABSOLUES :
- Ne JAMAIS faire de 'import' de classes de mcnptools autre que 'from mcnptools import Ptrac'
- Ne JAMAIS utiliser les attributs internes (ex: m_events, m_type) — uniquement les méthodes publiques
- Utilise la variable ptrac_path = '<PTRAC_PATH_PLACEHOLDER>' comme chemin du fichier PTRAC (pas de chemin en dur)
- Toujours utiliser la méthode ReadHistories() pour récupérer les histoires des particules

---

BONNES PRATIQUES :
1. Les dictionnaires comme PtracReactionDict (MT_xx), ParticleCodeDict, PtracZAIDDict sont des structures internes du KG :
   - Ne JAMAIS les importer
   - Si tu en utilises un, accède à son champ 'value', jamais son 'id' (ex: utilise 1, pas PARTICLE_1)

2. Avant tout appel à 'event.Get(...)', vérifie sa présence avec 'event.Has(...)' :
   Correct :
   if event.Has(Ptrac.X):
       x = event.Get(Ptrac.X)

3. Les entités ENUMS de type BNK ou TER s'appellent toujours de cette façon : Ptrac.ENUM
   (exemples :  Ptrac.BNK_KNOCK_ON ; Ptrac.TER_E_BREMSSTRAHLUNG)

---

COMPRÉHENSION DES HISTOIRES ET PARTICULES :

Chaque fichier PTRAC contient des HISTOIRES de simulation (track histories).  
Chaque histoire inclut une ou plusieurs PARTICULES. Chaque particule est représentée par une SÉQUENCE D'ÉVÉNEMENTS consécutifs :

- Elle commence toujours par un événement SRC ou BNK.
- Elle se termine toujours par un événement TER.

Une particule ≠ un événement. Une particule génère plusieurs événements consécutifs.  
Dans une même histoire, on peut avoir 1 particule SRC suivie de plusieurs particules secondaires issues de BNK.

Ne pas confondre :
  - Le nombre d’événements (COL, SUR, etc.)
  - Le nombre de particules (chaque SRC/BNK génère une)
  - Le nombre d’histoires (une entrée de simulation)

---

TRAÇAGE D'UNE PARTICULE DANS UNE HISTOIRE :

Pour suivre la trajectoire d'une particule :
- Repérer un événement de type SRC ou BNK
- Collecter tous les événements qui suivent, appartenant à cette même particule
- Arrêter à l’événement TER correspondant

Critère d’appartenance : les événements d’une particule sont consécutifs dans la liste, entre le SRC/BNK initial et le TER final.

Chaque particule suit donc un chemin unique :  
  [ SRC ] → COL → COL → SUR → … → TER  
  [ BNK ] → COL → SUR → COL → … → TER

---

CALCULS TYPIQUES SUR UNE PARTICULE (et erreurs fréquentes à éviter) :

• Énergie déposée :
   - Prendre l’énergie du premier événement (SRC ou BNK)
     if event.Type() == Ptrac.SRC or Ptrac.BNK:
         energy_init = event.Get(Ptrac.ENERGY)
   - Parcourir jusqu’au TER correspondant
     if event.Type() == Ptrac.TER:
         energy_final = event.Get(Ptrac.ENERGY)
   - Calcul : energy_init - energy_final

• Temps de vol :
   - time_depart = event.Get(Ptrac.TIME) au SRC ou BNK
   - time_arrivee = event.Get(Ptrac.TIME) au TER
   - Calcul : time_arrivee - time_depart

Ne JAMAIS :
   - additionner les énergies de tous les événements COL
   - inclure les événements de la particule suivante (après le TER)

---

STRUCTURE ATTENDUE DE LA RÉPONSE :
1. Explication en langage naturel (claire, pédagogique, structurée)
2. Bloc de code Python dans ```python ... ``` avec indentation correcte

Raisonne étape par étape avant de coder.

"""
