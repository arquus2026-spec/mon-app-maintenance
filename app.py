import streamlit as st
from datetime import date

# ---------------------------
# INIT SESSION
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

if "maintenance_tab" not in st.session_state:
    st.session_state.maintenance_tab = "dashboard"

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(layout="wide")

# ---------------------------
# STYLE
# ---------------------------
st.markdown("""
<style>
.stApp {
    background-color: #F5F6F8;
    color: #1C1C1C;
}

section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E0E0E0;
}

div.stButton > button {
    width: 100%;
    background-color: transparent;
    border: none;
    text-align: left;
    padding: 10px;
}

div.stButton > button:hover {
    background-color: #E9ECEF;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 6px;
    border: 1px solid #E0E0E0;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("NAVIGATION")

if st.sidebar.button("Accueil"):
    st.session_state.page = "Accueil"

if st.sidebar.button("Gestion Maintenance"):
    st.session_state.page = "Maintenance"

if st.sidebar.button("Intervenant extérieur"):
    st.session_state.page = "Ext"

if st.sidebar.button("Opérateur"):
    st.session_state.page = "Operateur"

if st.sidebar.button("Technicien site"):
    st.session_state.page = "Tech"

# ---------------------------
# ACCUEIL
# ---------------------------
if st.session_state.page == "Accueil":
    st.title("ENTRETIEN | AIRE DE LAVAGE – ARQUUS")
    st.write(date.today())

# ---------------------------
# PAGE MAINTENANCE
# ---------------------------
elif st.session_state.page == "Maintenance":

    st.title("Gestion Maintenance")

    col_menu, col_content = st.columns([1, 4])

    # MENU
    with col_menu:
        if st.button("Tableau de bord"):
            st.session_state.maintenance_tab = "dashboard"

        if st.button("Calendrier"):
            st.session_state.maintenance_tab = "calendar"

        if st.button("Contrôle périodique"):
            st.session_state.maintenance_tab = "control"

        if st.button("Compteurs"):
            st.session_state.maintenance_tab = "counters"

        if st.button("Intervenants"):
            st.session_state.maintenance_tab = "intervenants"

        if st.button("Historique"):
            st.session_state.maintenance_tab = "history"

    # CONTENU
    with col_content:

        tab = st.session_state.maintenance_tab

        # ---------------- DASHBOARD
        if tab == "dashboard":
            st.subheader("Tableau de bord")
            col1, col2, col3 = st.columns(3)
            col1.metric("Équipements", "24")
            col2.metric("Maintenances", "3")
            col3.metric("Alertes", "1")

        # ---------------- CALENDRIER
        elif tab == "calendar":
            st.subheader("Calendrier")
            st.info("À connecter")

        # ---------------- CONTROLE PERIODIQUE
        elif tab == "control":
            st.subheader("Contrôle périodique")

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.write("Créer / modifier une gamme")

            nom_gamme = st.text_input("Nom de la gamme")
            frequence = st.selectbox("Fréquence", ["Journalier", "Hebdomadaire", "Mensuel"])
            lien = st.text_input("Lien (OneDrive / Doc)")

            if st.button("Enregistrer la gamme"):
                st.success("Gamme enregistrée")

            st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- COMPTEURS
        elif tab == "counters":
            st.subheader("Compteurs")

            st.number_input("Heures machine", 0, 5000, 1200)
            st.number_input("Cycles", 0, 10000, 350)

        # ---------------- INTERVENANTS
        elif tab == "intervenants":
            st.subheader("Intervenants")

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.text_input("Nom / Libellé")
            st.text_input("Rôle")
            st.text_input("Téléphone")
            st.text_input("Email")
            st.text_input("Contact principal")

            ext = st.checkbox("Intervenant extérieur")

            st.write("Couleur")
            cols = st.columns(8)
            for i in range(8):
                cols[i].button(" ", key=f"c{i}")

            st.markdown("---")

            st.write("Gammes associées")

            st.text_input("Gamme 1 (lien)")
            st.text_input("Gamme 2 (lien)")

            if st.button("Ajouter intervenant"):
                st.success("Intervenant enregistré")

            st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- HISTORIQUE
        elif tab == "history":
            st.subheader("Historique")
            st.table({
                "Date": ["17/04/2026"],
                "Action": ["Contrôle"],
                "Intervenant": ["Dupont"]
            })

# ---------------------------
# AUTRES MODULES
# ---------------------------
elif st.session_state.page == "Ext":
    st.title("Intervenants extérieurs")
    st.write("Liste + gestion des prestataires externes")

elif st.session_state.page == "Operateur":
    st.title("Opérateurs")
    st.write("Gestion des opérateurs")

elif st.session_state.page == "Tech":
    st.title("Techniciens site")
    st.write("Gestion des techniciens internes")
