# Wine Quality Prediction

## Description

Ce projet consiste à développer une solution de Machine Learning permettant de prédire la qualité d'un vin à partir de ses caractéristiques physico-chimiques.

L'objectif est de classer les vins en trois catégories :

Low: qualité faible
Medium : qualité moyenne
High : qualité élevée

Le projet couvre l'ensemble du processus, de l'exploration des données jusqu'au déploiement du modèle avec FastAPI et Streamlit.


## Objectifs du projet

Les principaux objectifs sont :

Explorer et comprendre le dataset Wine Quality
Nettoyer et préparer les données
Analyser les relations entre les variables
Transformer la variable quality en catégories
Entraîner plusieurs modèles de Machine Learning
Évaluer les performances des modèles
Sélectionner un modèle performant
Sauvegarder le modèle et le préprocesseur
Développer une API de prédiction avec FastAPI
Créer une interface utilisateur avec Streamlit



## Analyse exploratoire

L'analyse exploratoire des données comprend notamment :

Analyse des valeurs manquantes
Détection des doublons
Statistiques descriptives
Analyse des distributions
Analyse des valeurs aberrantes
Matrice de corrélation
Visualisation des relations entre les variables
Analyse de la distribution de la variable cible
Analyse en composantes principales (PCA)

Quelques relations importantes observées :

alcohol présente une corrélation positive avec quality
density présente une corrélation négative avec quality
volatile acidity présente également une corrélation négative avec quality


##  Prétraitement des données

Les principales étapes de préparation sont :

Suppression des doublons
Séparation des variables explicatives et de la cible
Séparation des données en train/test
Standardisation des variables numériques avec StandardScaler
Encodage de la variable catégorielle type avec OneHotEncoder
Gestion du déséquilibre des classes avec class_weight="balanced

Le préprocesseur est sauvegardé séparément afin de garantir que les nouvelles données reçues par l'API subissent exactement le même traitement que les données d'entraînement.

---

## Modélisation

Plusieurs modèles ont été testés :

Logistic Regression
Random Forest
Gradient Boosting


##  API FastAPI

Une API REST a été développée avec FastAPI.

L'API possède notamment l'endpoint :

text
POST /predict


Elle reçoit les caractéristiques d'un vin et retourne sa classe prédite.



### Lancer l'API

Après installation des dépendances :

bash
uvicorn api.main:app --reload


L'API sera disponible à :

text
http://127.0.0.1:8000


La documentation interactive Swagger est disponible à :

text
http://127.0.0.1:8000/docs


## Interface Streamlit

Une interface utilisateur a été développée avec Streamlit.

Elle permet à l'utilisateur de :

Entrer les caractéristiques d'un vin
Choisir le type de vin
Envoyer les données à l'API
Obtenir la qualité prédite

### Lancer Streamlit

bash
streamlit run streamlit_app.py


L'application sera disponible sur :

text
http://localhost:8501




##  Installation

### 1. Cloner le projet

bash
git clone https://github.com/Kiritosexy/-wine-quality-prediction.git

### 2. Accéder au projet

bash
cd WINE_QUALITY


### 3. Créer un environnement virtuel

Windows :

powershell
python -m venv venv


### 4. Activer l'environnement

powershell
.\venv\Scripts\Activate.ps1


### 5. Installer les dépendances

bash
pip install -r requirements.txt



## Utilisation

### Terminal 1 — FastAPI

bash
uvicorn api.main:app --reload


### Terminal 2 — Streamlit

bash
streamlit run streamlit_app.py


## Technologies utilisées

 Python
 Pandas
 NumPy
 Scikit-learn
 Matplotlib
 Seaborn
 Joblib
 FastAPI
 Pydantic
 Uvicorn
 Streamlit


##  Limites du projet

Le modèle présente certaines limites :

Les performances restent perfectibles
Les classes de qualité ne sont pas parfaitement équilibrées
La classification en trois catégories simplifie la variable quality
Les performances dépendent fortement de la qualité des données utilisées pour l'entraînement


##  Perspectives d'amélioration

Plusieurs améliorations pourraient être envisagées :

Optimisation des hyperparamètres
Comparaison avec XGBoost ou LightGBM
Utilisation de techniques avancées de rééquilibrage
Cross-validation
Amélioration de l'interface Streamlit
Conteneurisation avec Docker
Mise en place de MLflow pour le suivi des expériences
Déploiement cloud de l'API et de l'application



## Licence

Ce projet est réalisé à des fins académiques et pédagogiques.
