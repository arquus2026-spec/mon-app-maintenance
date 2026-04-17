import streamlit as st
from datetime import date

# ---------------------------
# INIT NAVIGATION
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

if "maintenance_tab" not in st.session_state:
    st.session_state.maintenance_tab = "dashboard"

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(
    page_title="ARQUUS - Maintenance",
    layout="wide"
)

# ---------------------------
# STYLE (BLANC + INDUSTRIEL)
# ---------------------------
st.markdown("""
<style>
.stApp {
    background-color: #F5F6F8;
    color: #1C1C1C;
}

/* TITRES */
h1, h2, h3 {
    color: #1C1C1C;
    font-weight: 500;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E0E0E0;
}

/* BOUTONS MENU */
div.stButton > button {
    width: 100%;
    background-color: transparent;
    border: none;
    color: #333;
    text-align: left;
    padding: 10px;
    border-radius: 4px;
}

div.stButton > button:hover {
    background-color: #E9ECEF;
}

/* CARDS */
.card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 6px;
    border: 1px solid #E0E0E0;
    margin-bottom: 15px;
}

/* INPUTS */
input, textarea {
    background-color: #FFFFFF !important;
    color: #000 !important;
}

/* METRICS */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 15px;
    border-radius: 6px;
    border: 1px solid #E0E0E0;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR NAV
# ---------------------------
st.sidebar.markdown("### NAVIGATION")

if st.sidebar.button("Accueil"):
    st.session_state.page = "Accueil"

if st.sidebar.button("Gestion Maintenance"):
    st.session_state.page = "Maintenance"

# ---------------------------
# PAGE ACCUEIL
# ---------------------------
if st.session_state.page == "Accueil":
    st.title("ENTRETIEN | AIRE DE LAVAGE – ARQUUS")

    aujourdhui = date.today().strftime("%d / %m / %Y")
    st.write(f"Date : {aujourdhui}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Gestion Maintenance"):
            st.session_state.page = "Maintenance"
            st.rerun()

# ---------------------------
# PAGE MAINTENANCE
# ---------------------------
elif st.session_state.page == "Maintenance":

    st.title("Gestion Maintenance")

    col_menu, col_content = st.columns([1, 4])

    # -------- MENU GAUCHE
    with col_menu:
        st.markdown("### Navigation")

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

    # -------- CONTENU
    with col_content:

        tab = st.session_state.maintenance_tab

        # DASHBOARD
        if tab == "dashboard":
            st.subheader("Tableau de bord")

            col1, col2, col3 = st.columns(3)
            col1.metric("Équipements", "24")
            col2.metric("Maintenances", "3")
            col3.metric("Alertes", "1")

        # CALENDRIER
        elif tab == "calendar":
            st.subheader("Calendrier")
            st.info("Module calendrier à connecter")

        # CONTROLES
        elif tab == "control":
            st.subheader("Contrôles périodiques")

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.checkbox("Contrôle journalier")
            st.checkbox("Contrôle hebdomadaire")
            st.markdown('</div>', unsafe_allow_html=True)

        # COMPTEURS
        elif tab == "counters":
            st.subheader("Compteurs")

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.number_input("Heures machine", 0, 5000, 1200)
            st.number_input("Cycles", 0, 10000, 350)
            st.markdown('</div>', unsafe_allow_html=True)

        # INTERVENANTS
        elif tab == "intervenants":
            st.subheader("Intervenants")

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.text_input("Nom / Libellé")
            st.text_input("Rôle")
            st.text_input("Téléphone")
            st.text_input("Email")

            st.checkbox("Intervenant extérieur")

            st.write("Couleur")
            cols = st.columns(10)
            for i in range(10):
                cols[i].button(" ", key=f"color_{i}")

            if st.button("Ajouter"):
                st.success("Intervenant ajouté")

            st.markdown('</div>', unsafe_allow_html=True)

        # HISTORIQUE
        elif tab == "history":
            st.subheader("Historique")

            st.table({
                "Date": ["17/04/2026"],
                "Action": ["Contrôle effectué"],
                "Intervenant": ["Dupont"]
            })
