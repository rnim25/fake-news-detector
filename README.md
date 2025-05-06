# Fake News Detector

##  Description
**Fake News Detector** est une application de détection de fausses informations basée sur l'intelligence artificielle. Elle permet d’analyser du contenu textuel en français, anglais, arabe ou dialecte tunisien pour déterminer s’il est fiable ou non. Ce projet s'appuie sur un modèle BERT entraîné sur des jeux de données multilingues.

L’application a été développée dans le cadre d’un projet académique en intelligence artificielle, avec une attention particulière portée à la modularité, la reproductibilité et l'accessibilité.

##  Fonctionnalités principales
- Analyse de texte multilingue (FR, EN, AR, TUN)
- Prédiction binaire : **Fake** ou **Real**
- Interface utilisateur via **Streamlit**
- Modèle pré-entraîné avec affichage du résultat en temps réel

### 1. Cloner le projet
```bash
git clone https://github.com/tonutilisateur/fake-news-detector.git
cd fake-news-detector

# 1. Créer un environnement virtuel
python -m venv venv

# 2. Activer l’environnement virtuel

# Sur Linux/macOS :
source venv/bin/activate

# Sur Windows :
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
