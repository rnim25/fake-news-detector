import streamlit as st
import pickle

st.title("📰 Fake News Detector")

st.write("Collez ici un texte d'article pour vérifier s'il est fiable ou pas.")

user_input = st.text_area("Texte de l'article")

if user_input:
    # FAUX modèle juste pour la démo
    if "vaccin" in user_input.lower() or "complot" in user_input.lower():
        st.error("🛑 FAKE News détectée !")
    else:
        st.success("✅ Cette nouvelle semble réelle.")

# Charger le modèle depuis le fichier
with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📰 Détecteur de Fake News")

text = st.text_area("Entrez le texte à analyser")

if text:
    prediction = model.predict([text])
    if prediction[0] == 1:
        st.success("✅ Cette nouvelle semble réelle.")
    else:
        st.error("🛑 FAKE News détectée !")
