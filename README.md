# Algorithmes de Clustering
Projet d'analyse et d'implémentation d'algorithmes de classification non supervisée

## 📑 Sommaire

1. [Contexte du projet](#contexte-du-projet)
2. [Veille technologique](#veille-technologique)
   - [Algorithmes de classification non supervisée](#algorithmes-de-classification-non-supervisée)
   - [Méthodes de sélection du nombre optimal de clusters](#méthodes-de-sélection-du-nombre-optimal-de-clusters)
   - [Mesures de qualité d'un cluster](#mesures-de-qualité-dun-cluster)
3. [Implémentation K-means et application sur Iris](#implémentation-k-means-et-application-sur-iris)
   - [Classe K-means personnalisée](#classe-k-means-personnalisée)
   - [Application sur le dataset Iris](#application-sur-le-dataset-iris)
   - [Comparaison avec Scikit-Learn](#comparaison-avec-scikit-learn)
4. [Analyse du dataset Customer Personality](#analyse-du-dataset-customer-personality)
   - [Exploration et analyse des données](#exploration-et-analyse-des-données)
   - [Préparation des données](#préparation-des-données)
   - [Réduction de dimension](#réduction-de-dimension)
5. [Application des algorithmes de clustering](#application-des-algorithmes-de-clustering)
   - [K-Means](#k-means)
   - [Hierarchical Clustering](#hierarchical-clustering)
   - [DBSCAN](#dbscan)
   - [Comparaison des algorithmes](#comparaison-des-algorithmes)
6. [Évaluation et optimisation](#évaluation-et-optimisation)
   - [Détermination du nombre optimal de clusters](#détermination-du-nombre-optimal-de-clusters)
   - [Métriques d'évaluation](#métriques-dévaluation)
7. [Profiling des groupes de clients](#profiling-des-groupes-de-clients)
8. [Conclusion](#conclusion)

---

## Contexte du projet

Ce projet vise à étudier et appliquer les algorithmes de classification non supervisée (clustering) dans le cadre d'une analyse de données clients. Il se compose de deux parties principales :

1. **Étude théorique et pratique des algorithmes de clustering** : Implémentation d'une classe K-means personnalisée et application sur le dataset Iris
2. **Analyse complète d'un dataset client** : Application de plusieurs algorithmes de clustering sur des données de marketing pour segmenter la clientèle

### Objectifs
- Comprendre le fonctionnement des algorithmes de clustering
- Implémenter l'algorithme K-means from scratch
- Évaluer et comparer différents algorithmes de clustering
- Analyser les caractéristiques des groupes de clients identifiés

---

## Veille technologique

### Algorithmes de classification non supervisée

#### 1. K-Means
**Principe** : Algorithme de partitionnement qui divise les données en k clusters en minimisant la variance intra-cluster.

**Fonctionnement** :
- Initialisation aléatoire de k centroïdes
- Assignation de chaque point au centroïde le plus proche
- Mise à jour des centroïdes (moyenne des points assignés)
- Répétition jusqu'à convergence

**Avantages** :
- Simple à comprendre et implémenter
- Efficace sur de grands datasets
- Fonctionne bien avec des clusters sphériques

**Inconvénients** :
- Nécessite de spécifier k à l'avance
- Sensible à l'initialisation
- Assume des clusters de forme sphérique

#### 2. Hierarchical Clustering (Classification Hiérarchique)
**Principe** : Crée une hiérarchie de clusters par fusion (agglomérative) ou division (divisive) successive.

**Fonctionnement** :
- Agglomératif : Commence avec chaque point comme cluster, fusionne les plus proches
- Divisif : Commence avec un seul cluster, divise récursivement
- Utilise une matrice de distances et un critère de liaison

**Avantages** :
- Pas besoin de spécifier le nombre de clusters à l'avance
- Produit un dendrogramme informatif
- Déterministe (pas d'aléatoire)

**Inconvénients** :
- Complexité O(n³) pour n points
- Sensible aux outliers
- Difficile à modifier une fois construit

#### 3. DBSCAN (Density-Based Spatial Clustering)
**Principe** : Groupe les points qui sont étroitement regroupés et marque les points isolés comme outliers.

**Fonctionnement** :
- Utilise deux paramètres : eps (rayon) et min_samples (points minimum)
- Identifie les points core, border et noise
- Forme des clusters basés sur la densité

**Avantages** :
- Peut trouver des clusters de forme arbitraire
- Robuste aux outliers
- Détermine automatiquement le nombre de clusters

**Inconvénients** :
- Sensible aux paramètres eps et min_samples
- Difficile avec des densités variables
- Performance dégradée en haute dimension

### Méthodes de sélection du nombre optimal de clusters

#### Méthode du coude (Elbow Method)
**Principe** : Trace la variance intra-cluster en fonction du nombre de clusters et cherche le "coude" de la courbe.

**Mise en œuvre** :
- Calcule la somme des carrés intra-cluster (WCSS) pour différentes valeurs de k
- Trace WCSS vs k
- Identifie le point où la décroissance devient moins prononcée

**Limites** :
- Subjectif dans l'identification du coude
- Peut être ambigu si plusieurs coudes existent

#### Silhouette Score
**Principe** : Mesure la qualité du clustering en comparant la cohésion intra-cluster et la séparation inter-cluster.

**Calcul** :
- Pour chaque point : s(i) = (b(i) - a(i)) / max(a(i), b(i))
- a(i) : distance moyenne aux points du même cluster
- b(i) : distance moyenne au cluster le plus proche

**Interprétation** :
- Score entre -1 et 1
- Plus proche de 1 = meilleur clustering
- Négatif = point mal classé

#### Gap Statistic
**Principe** : Compare la variance intra-cluster observée avec celle attendue sous une distribution uniforme.

**Avantages** :
- Approche statistique rigoureuse
- Moins subjective que la méthode du coude
- Fournit une estimation statistique du nombre optimal

**Mise en œuvre** :
- Génère des données de référence uniformes
- Compare la log(WCSS) observée vs référence
- Choisit k où le gap est maximal

### Mesures de qualité d'un cluster

#### Cohésion intra-cluster
**Mesures de compacité** :
- Somme des carrés intra-cluster (WCSS)
- Distance moyenne des points au centroïde
- Variance intra-cluster

**Objectif** : Minimiser la dispersion des points au sein de chaque cluster

#### Séparation inter-cluster
**Mesures de séparation** :
- Distance entre centroïdes
- Somme des carrés inter-cluster (BCSS)
- Distance minimum entre clusters

**Objectif** : Maximiser la distance entre les différents clusters

#### Indices de validité
**Indices internes** :
- Calinski-Harabasz Index : Rapport BCSS/WCSS
- Davies-Bouldin Index : Moyenne des ratios intra/inter-cluster
- Dunn Index : Ratio distance min inter/max intra

**Indices externes** (si vérité terrain disponible) :
- Adjusted Rand Index (ARI)
- Normalized Mutual Information (NMI)
- Homogeneity, Completeness, V-measure

---

## Implémentation K-means et application sur Iris

### Classe K-means personnalisée
Implémentation from scratch de l'algorithme K-means avec :
- Initialisation aléatoire des centroïdes
- Assignation des points aux clusters
- Mise à jour itérative des centroïdes
- Critère de convergence

### Application sur le dataset Iris
**Objectifs** :
- Tester la classe K-means personnalisée
- Comparer avec l'implémentation Scikit-Learn
- Analyser la stabilité sur plusieurs exécutions
- Évaluer pour différentes valeurs de k

**Observations attendues** :
- Variabilité des résultats due à l'initialisation aléatoire
- Impact du nombre de clusters sur la qualité
- Différences potentielles avec Scikit-Learn

### Comparaison avec Scikit-Learn
Comparaison des performances, stabilité et résultats entre :
- Implémentation personnalisée
- sklearn.cluster.KMeans
- Analyse des différences et similitudes

---

## Analyse du dataset Customer Personality

### Exploration et analyse des données
**Dataset** : Marketing Campaign (Customer Personality Analysis)
- **Source** : Données de campagne marketing d'une épicerie
- **Variables** : Démographiques, comportementales, transactionnelles
- **Objectif** : Segmentation client pour ciblage marketing

**Analyse exploratoire** :
- Statistiques descriptives
- Visualisations des distributions
- Identification des variables pertinentes
- Détection d'outliers et valeurs manquantes

### Préparation des données
**Étapes de preprocessing** :
- Nettoyage des données (valeurs manquantes, outliers)
- Encodage des variables catégorielles
- Normalisation/standardisation des variables numériques
- Gestion des variables dérivées (âge, ancienneté client)

### Réduction de dimension
**Sélection de features** :
- Analyse de corrélation
- Importance des variables
- Élimination des variables redondantes

**Analyse factorielle multiple (MFA)** :
- Réduction de la dimensionnalité
- Préservation de l'information pertinente
- Visualisation en 2D/3D

---

## Application des algorithmes de clustering

### K-Means
**Implémentation** :
- Application de l'algorithme pour différentes valeurs de k
- Analyse de la stabilité sur plusieurs exécutions
- Utilisation de k-means++ pour l'initialisation

**Paramètres testés** :
- Nombre de clusters : 2 à 10
- Différentes initialisations
- Critères de convergence

### Hierarchical Clustering
**Implémentation** :
- Clustering agglomératif
- Différents critères de liaison (ward, complete, average)
- Construction et analyse du dendrogramme

**Analyse** :
- Dendrogramme pour visualiser la hiérarchie
- Seuil de coupure pour déterminer le nombre de clusters
- Comparaison des critères de liaison

### DBSCAN
**Implémentation** :
- Recherche des paramètres optimaux (eps, min_samples)
- Analyse des outliers détectés
- Évaluation de la robustesse

**Paramètres** :
- eps : Distance maximale entre points voisins
- min_samples : Nombre minimum de points pour former un cluster
- Analyse de sensibilité aux paramètres

### Comparaison des algorithmes
**Critères de comparaison** :
- Qualité des clusters (silhouette, inertie)
- Stabilité des résultats
- Temps d'exécution
- Facilité d'interprétation
- Robustesse aux outliers

---

## Évaluation et optimisation

### Détermination du nombre optimal de clusters
**Méthodes appliquées** :
- Méthode du coude (Elbow Method)
- Silhouette Score
- Gap Statistic
- Calinski-Harabasz Index

**Analyse comparative** :
- Convergence des différentes méthodes
- Choix du nombre optimal de clusters
- Validation croisée des résultats

### Métriques d'évaluation
**Scores calculés** :
- Silhouette Score par cluster et global
- Inertie intra-cluster
- Indices de validité interne
- Stabilité sur différentes exécutions

**Interprétation** :
- Analyse des scores obtenus
- Comparaison entre algorithmes
- Choix du modèle final

---

## Profiling des groupes de clients

**Caractérisation des clusters** :
- Profil démographique (âge, éducation, situation familiale)
- Comportement d'achat (montants, fréquence, canaux)
- Réponse aux campagnes marketing
- Préférences produits

**Insights business** :
- Segments de clientèle identifiés
- Stratégies de ciblage recommandées
- Opportunités de cross-selling/up-selling
- Personnalisation des offres

**Visualisations** :
- Graphiques radar des profils
- Heatmaps des caractéristiques
- Analyse des correspondances
- Projections 2D/3D des clusters

---

## Conclusion

### Synthèse du travail réalisé
- Étude théorique des algorithmes de clustering
- Implémentation pratique d'une classe K-means
- Application sur datasets réels (Iris et Customer Personality)
- Comparaison et évaluation des différents algorithmes

### Apprentissages clés
- Importance du preprocessing des données
- Impact des paramètres sur les résultats
- Nécessité d'utiliser plusieurs métriques d'évaluation
- Complémentarité des différents algorithmes

### Perspectives d'amélioration
- Test d'autres algorithmes (GMM, Mean Shift)
- Optimisation des hyperparamètres
- Validation temporelle des segments
- Intégration de données externes

---

## 📁 Structure du projet

```
customer-personality-analysis/
├── data/
│   └── raw/
│       └── marketing_campaign.csv    # Dataset principal de marketing
├── exploration.ipynb                 # Analyse exploratoire des données
├── modelisation.ipynb                # Application des algorithmes de clustering
├── kmeans.py                         # Implémentation classe K-means personnalisée
└── README.md                         # Documentation du projet
```

## 🚀 Comment utiliser ce projet

### Prérequis
```bash
pip install numpy pandas scikit-learn matplotlib seaborn jupyter
```

### Étapes d'exécution
1. **Exploration des données** : Lancez `exploration.ipynb` pour l'analyse exploratoire
2. **Test sur Iris** : Utilisez `kmeans.py` pour tester l'implémentation K-means sur Iris
3. **Modélisation** : Exécutez `modelisation.ipynb` pour l'application des algorithmes de clustering
4. **Analyse** : Interprétez les résultats et profilez les segments clients

### Notebooks
- `exploration.ipynb` : Analyse exploratoire, preprocessing, réduction de dimension
- `modelisation.ipynb` : Application K-means, Hierarchical Clustering, DBSCAN et évaluation

## 📚 Ressources et références

### Algorithmes de clustering
- [Scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [K-means Clustering](https://en.wikipedia.org/wiki/K-means_clustering)
- [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN)

### Métriques d'évaluation
- [Silhouette Analysis](https://scikit-learn.org/stable/modules/clustering.html#silhouette-analysis)
- [Calinski-Harabasz Index](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index)

### Dataset
- [Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)
- [Iris Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)