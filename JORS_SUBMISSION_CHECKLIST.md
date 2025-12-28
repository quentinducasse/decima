# JORS Submission Checklist pour DECIMA Paper

## ✅ Éléments Complétés

### Métadonnées
- [x] Titre clair et descriptif
- [x] Liste des auteurs avec ORCID
- [x] Affiliations complètes
- [x] Date de publication (December 2025)
- [x] Keywords (8 keywords fournis)
- [x] Abstract (<150 mots recommandé)

### Structure du Paper
- [x] Section (1) Overview avec Introduction et Implementation
- [x] Section (2) Availability avec toutes les informations requises
- [x] Section (3) Reuse potential
- [x] Section (4) Quality control avec validation quantitative
- [x] Funding Statement
- [x] Competing Interests
- [x] Acknowledgements
- [x] References (bibliographie)

### Figures
- [x] Figure 1 : Architecture workflow (89 KB)
- [x] Figure 2 : Interface web (121 KB)
- [x] Figure 3 : Validation MCTAL vs PTRAC (91 KB)
- [x] Toutes les légendes sont auto-suffisantes
- [x] Toutes les figures sont référencées dans le texte
- [x] Formats appropriés (JPEG/PNG)
- [x] Taille raisonnable (<150 KB chacune)

### Contenu Technique
- [x] Description de MCNPToolsPro et son rôle
- [x] Architecture multi-agents détaillée
- [x] Validation quantitative avec statistiques
- [x] Explication des différences MCTAL vs PTRAC
- [x] Instructions d'installation (Docker + native)
- [x] Informations sur les dépendances
- [x] Licence (Apache 2.0)
- [x] Lien GitHub et DOI Zenodo

## 📝 Actions Avant Soumission

### 1. Vérifications Éditoriales
- [ ] Relecture complète pour fautes de frappe
- [ ] Vérifier cohérence des acronymes (première utilisation définie)
- [ ] Vérifier numérotation des sections
- [ ] Vérifier formatage des références bibliographiques

### 2. Fichiers à Préparer
- [ ] Créer `paper.bib` avec toutes les références citées :
  - [ ] @mcnptools2022
  - [ ] @easyptrac2018
  - [ ] @pyne2019
  - [ ] @sandy2021
  - [ ] @f4enix2021
  - [ ] @mctools2020
  - [ ] @mcnpy2022
  - [ ] @Cypher2018
- [ ] Convertir paper_jors.md en format requis par JORS (probablement LaTeX ou DOCX)
- [ ] S'assurer que les chemins des figures fonctionnent dans le format final

### 3. Vérifications Techniques
- [ ] Tester tous les liens URL (GitHub, Zenodo, MCNPToolsPro)
- [ ] Vérifier que le DOI Zenodo est à jour (actuellement 1.3.2, passage à 1.4.0)
- [ ] Mettre à jour le Zenodo avec la version 1.4.0 avant soumission
- [ ] Vérifier que la date "September 2025" pour GitHub (ligne 113) est cohérente avec "December 2025" pour Zenodo

### 4. Améliorations Optionnelles
- [ ] Ajouter une table des caractéristiques comparatives (DECIMA vs autres outils)
- [ ] Considérer l'ajout d'un exemple de code court en annexe
- [ ] Vérifier si JORS accepte du matériel supplémentaire (supplementary materials)

### 5. Conformité JORS
- [ ] Vérifier le guide de soumission JORS : https://openresearchsoftware.metajnl.com/about/submissions/
- [ ] Format de citation approprié
- [ ] Longueur du paper (pas de limite stricte mais ~3000-5000 mots recommandé)
- [ ] Tous les auteurs ont approuvé la version finale

## 🔧 Points à Vérifier Spécifiquement

### Incohérences potentielles
- **Date GitHub** : Ligne 113 dit "September 2025" alors que Zenodo dit "December 2025"
  - → Harmoniser à "December 2025" ?

### Références manquantes dans paper.bib
Actuellement cité mais non défini :
1. @mcnptools2022 (MCNPTools)
2. @easyptrac2018 (Easy-PTRAC)
3. @pyne2019 (PyNE)
4. @sandy2021 (SANDY)
5. @f4enix2021 (F4Enix)
6. @mctools2020 (mc-tools)
7. @mcnpy2022 (MCNPy)
8. @Cypher2018 (Cypher queries)

## 📊 Statistiques du Paper

- **Mots (approximatif)** : ~3,500 mots
- **Sections** : 4 sections principales + métadonnées
- **Figures** : 3 figures (301 KB total)
- **Références** : 8 citations
- **Auteurs** : 2 auteurs avec ORCID

## 🎯 Prochaines Étapes Recommandées

1. **Immédiat** :
   - Créer le fichier `paper.bib` avec toutes les références
   - Harmoniser les dates (September vs December)
   - Relecture finale

2. **Avant soumission** :
   - Mettre à jour Zenodo avec version 1.4.0
   - Vérifier tous les liens fonctionnent
   - Convertir au format requis par JORS

3. **Lors de la soumission** :
   - Uploader le paper + figures séparément si requis
   - Fournir tous les métadonnées demandées
   - Suggérer des reviewers potentiels si demandé

## 📧 Contact JORS

- Site web : https://openresearchsoftware.metajnl.com/
- Email : info@openresearchsoftware.metajnl.com
- Guide auteurs : https://openresearchsoftware.metajnl.com/about/submissions/
