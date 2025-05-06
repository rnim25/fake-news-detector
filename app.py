import streamlit as st
import pickle
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Détecteur de Fake News", layout="wide")

# Chargement du modèle
with open("fake_news_model (3).pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

# Logo et titre
st.image("facke-news-removebg-preview.png", width=150)  
st.title("📰 Détecteur de Fake News")
st.markdown("Vérifiez si une nouvelle est vraie ou fausse grâce à une IA entraînée.")

# Zone de texte utilisateur
user_input = st.text_area("✏️ Collez ici votre texte :", height=150)

# Affiche le bouton UNIQUEMENT si du texte est entré
if user_input.strip():  # Si ce n’est pas vide ou juste des espaces
    if st.button("🔍 Analyser la news"):
        # Prédiction
        X_vec = vectorizer.transform([user_input])
        proba_real = model.predict_proba(X_vec)[0][1]
        proba_fake = 1 - proba_real

        # Deux colonnes : message à gauche, graphique à droite
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"### 🔎 Probabilité que ce soit une vraie news : **{proba_real * 100:.2f}%**")
            if proba_real > 0.5:
                st.success("✅ Cette nouvelle semble réelle.")
            else:
                st.error("🛑 FAKE News détectée !")

        with col2:
            labels = ['Fake', 'Real']
            sizes = [proba_fake, proba_real]
            colors = ['#FF4B4B', '#4CAF50']

            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)
