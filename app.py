import streamlit as st
import pickle
import matplotlib.pyplot as plt

# 🎨 Mise en page Streamlit
st.set_page_config(page_title="Détecteur de Fake News", layout="wide")

# 📌 Chargement du modèle
with open("facke-news-removebg-preview.png", "rb") as f:
    model = pickle.load(f)

# 🖼️ Affichage du logo
st.image("fake_news_model.pkl", width=80)  
st.title("📰 Détecteur de Fake News")
st.markdown("Vérifiez si une nouvelle est vraie ou fausse grâce à une IA entraînée.")

# 🧾 Entrée utilisateur
user_input = st.text_area("✏️ Collez ici votre texte :", height=150)

# ✅ Bouton pour déclencher l’analyse
if user_input.strip():
    if st.button("🔍 Analyser la news"):

        # 🔎 Prédiction
        proba_real = model.predict_proba([user_input])[0][1]
        proba_fake = 1 - proba_real

        # 👉 Deux colonnes : texte à gauche, graphique à droite
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

