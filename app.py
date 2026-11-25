
import streamlit as st

from associations import Utilisateur, associations, matching

# Configuration du site

st.set_page_config(
    page_title="ESCP Association Match",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 ESCP Association Match")

st.caption("Le Tinder des associations ESCP")

st.write(
    "Trouve l'association qui correspond le mieux "
    "à ta personnalité et à tes envies !"
)

st.divider()

# Questionnaire

st.header("📝 Ton profil")

with st.form("questionnaire"):

    categorie = st.selectbox(
        "Quelle catégorie t'intéresse ?",
        [
            "professionnelle",
            "vie de campus",
            "artistique",
            "musique",
            "culturelle",
            "humanitaire",
            "société",
            "sportive"
        ]
    )

    investissement = st.select_slider(
        "Combien souhaites-tu t'investir ?",
        options=["faible", "moyen", "fort"],
        value="moyen"
    )

    cotisation = st.selectbox(
        "Quel niveau de cotisation préfères-tu ?",
        ["faible", "moyen", "fort", "non"]
    )

    taille = st.radio(
        "Quelle taille d'association préfères-tu ?",
        ["petit", "moyen", "grand"],
        horizontal=True
    )

    experience_pro = st.selectbox(
        "Quelle expérience professionnelle recherches-tu ?",
        ["non", "faible", "moyen", "fort"]
    )

    voyage = st.radio(
        "Souhaites-tu voyager ?",
        ["oui", "non"],
        horizontal=True
    )

    diversite = st.radio(
        "Souhaites-tu une diversité internationale ?",
        ["oui", "non"],
        horizontal=True
    )

    envoyer = st.form_submit_button(
        "🔍 Découvrir mes associations",
        type="primary"
    )

# Algorithme de matching

if envoyer:

    utilisateur = Utilisateur(
        categorie,
        investissement,
        cotisation,
        taille,
        experience_pro,
        voyage,
        diversite
    )

    top3 = matching(utilisateur, associations)

    st.divider()

    st.header("🏆 Ton Top 3")

    st.balloons()

    medailles = ["🥇", "🥈", "🥉"]

    for i in range(len(top3)):

        association, score = top3[i]

        pourcentage = (score / 10) * 100

        with st.container(border=True):

            st.subheader(
                medailles[i] + " " + association.nom
            )

            st.metric(
                "Compatibilité",
                f"{pourcentage:.0f}%"
            )

            st.progress(pourcentage / 100)

            st.write("Catégorie :", association.categorie)
            st.write("Investissement :", association.investissement)
            st.write("Cotisation :", association.cotisation)
            st.write("Taille :", association.taille)
            st.write("Expérience pro :", association.experience_pro)

            if association.voyage == "oui":
                st.write("✈️ Possibilité de voyager")

            if association.diversite_internationale == "oui":
                st.write("🌍 Diversité internationale")

st.divider()

st.caption("Projet étudiant ESCP - Association Match")
