import streamlit as st

st.title("📰 Fake News Detector")

st.write("Collez ici un texte d'article pour vérifier s'il est fiable ou pas.")

user_input = st.text_area("Texte de l'article")

if user_input:
    # FAUX modèle juste pour la démo
    if "vaccin" in user_input.lower() or "complot" in user_input.lower():
        st.error("🛑 FAKE News détectée !")
    else:
        st.success("✅ Cette nouvelle semble réelle.")
