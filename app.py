import streamlit as st
from datetime import datetime, timedelta, date

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(layout="wide")

# ---------------------------
# INIT DATA
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

if "intervenants" not in st.session_state:
    st.session_state.intervenants = [
        {"nom": "Opérateurs", "type": "Opérateur"},
        {"nom": "Techniciens", "type": "Technicien"}
    ]

if "gammes" not in st.session_state:
    st.session_state.gammes = []

if "selected_intervenant" not in st.session_state:
    st.session_state.selected_intervenant = 0

# ---------------------------
# STYLE (BLANC PROPRE)
# ---------------------------
st.markdown("""
<style>
.stApp {
    background-color: #F5F6F8;
}

section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 1px solid #ddd;
}

.card {
    background-color: white;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 6px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# UTILS
# ---------------------------
def next_date(d, freq):
    map_days = {
        "1j":1,"1s":7,"2s":14,"1m":30,"3m":90,
        "6m":180,"1a":365,"2a":730,"3a":1095,
        "5a":1825,"10a":3650
    }
    return d + timedelta(days=map_days[freq])

def avoid_weekend(d):
    if d.weekday() == 5:
        return d + timedelta(days=2)
    if d.weekday() == 6:
        return d + timedelta(days=1)
    return d

# ---------------------------
# SIDEBAR NAV
# ---------------------------
st.sidebar.title("Navigation")

if st.sidebar.button("Accueil"):
    st.session_state.page = "Accueil"

if st.sidebar.button("Intervenants"):
    st.session_state.page = "Intervenants"

if st.sidebar.button("Gestion Maintenance"):
    st.session_state.page = "Maintenance"

# ---------------------------
# PAGE INTERVENANTS
# ---------------------------
if st.session_state.page == "Intervenants":

    col_left, col_right = st.columns([1, 3])

    # -------- LISTE GAUCHE
    with col_left:
        st.subheader("Intervenants")

        for i, inter in enumerate(st.session_state.intervenants):
            if st.button(inter["nom"], key=f"int_{i}"):
                st.session_state.selected_intervenant = i

        if st.button("Ajouter"):
            st.session_state.intervenants.append({"nom": "Nouveau", "type": ""})

    # -------- FORMULAIRE DROITE
    with col_right:
        i = st.session_state.selected_intervenant
        inter = st.session_state.intervenants[i]

        st.subheader("Modifier")

        nom = st.text_input("Nom", inter["nom"])
        type_i = st.selectbox("Type", ["Opérateur","Technicien","Externe"])

        if st.button("Sauvegarder"):
            st.session_state.intervenants[i]["nom"] = nom
            st.session_state.intervenants[i]["type"] = type_i

        if st.button("Supprimer"):
            st.session_state.intervenants.pop(i)
            st.rerun()

# ---------------------------
# PAGE MAINTENANCE
# ---------------------------
elif st.session_state.page == "Maintenance":

    tab = st.radio("Menu", ["Vue globale", "Nouvelle gamme"])

    # -------- VUE GLOBALE
    if tab == "Vue globale":

        st.subheader("Intervenants et gammes")

        for inter in st.session_state.intervenants:
            st.markdown(f"### {inter['nom']}")

            linked = [g for g in st.session_state.gammes if g["intervenant"] == inter["nom"]]

            if not linked:
                st.write("Aucune gamme")

            for g in linked:
                st.write(f"{g['frequence']} | {g['date']}")

    # -------- CREER GAMME
    if tab == "Nouvelle gamme":

        st.subheader("Créer une gamme")

        intervenant = st.selectbox(
            "Intervenant",
            [i["nom"] for i in st.session_state.intervenants]
        )

        frequence = st.selectbox("Fréquence", [
            "1j","1s","2s","1m","3m","6m","1a","2a","3a","5a","10a"
        ])

        date_depart = st.date_input("Date première intervention")

        lien = st.text_input("Lien / document")

        if st.button("Créer la gamme"):
            st.session_state.gammes.append({
                "intervenant": intervenant,
                "frequence": frequence,
                "date": date_depart,
                "lien": lien
            })
            st.success("Gamme créée")

        st.markdown("---")

        st.subheader("Modifier / Supprimer")

        for i, g in enumerate(st.session_state.gammes):
            st.write(g)

            col1, col2 = st.columns(2)

            if col1.button("Supprimer", key=f"sup_{i}"):
                st.session_state.gammes.pop(i)
                st.rerun()

# ---------------------------
# PAGE ACCUEIL = CALENDRIER
# ---------------------------
elif st.session_state.page == "Accueil":

    st.subheader("Calendrier (simulation)")

    for g in st.session_state.gammes:

        d = datetime.combine(g["date"], datetime.min.time())

        st.markdown(f"### {g['intervenant']}")

        for _ in range(10):
            d = next_date(d, g["frequence"])
            d = avoid_weekend(d)

            st.write(d.date())
