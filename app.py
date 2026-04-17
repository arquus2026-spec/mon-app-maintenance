import streamlit as st
from datetime import date

# ---------------------------
# INIT NAVIGATION
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

if "maintenance_tab" not in st.session_state:
    st.session_state.maintenance_tab = "Tableau de bord"

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(
    page_title="ARQUUS - Maintenance",
    layout="wide"
)

# ---------------------------
# STYLE (DA PROCHE SCREEN)
# ---------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0B0E14;
    color: #ADBAC7;
}

/* TITRE */
h1 {
    color: white;
    font-weight: 400;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #11151C;
}

/* BOUTONS MENU */
div.stButton > button {
    width: 100%;
    background-color: transparent;
    border: none;
    color: #ADBAC7;
    text-align: left;
    padding: 10px;
}

div.stButton > button:hover {
    background-color: #1C2128;
    color: white;
}

/* CARDS */
.card {
    background-color: #161B22;
    padding: 20px;
    border-radius: 6px;
    border: 1px solid #2D333B;
    margin-bottom: 15px;
}

/* LABEL */
.label {
    font-size: 12px;
    color: #5E6772;
    text-transform: uppercase;
}

/* INPUT */
input, textarea {
    background-color: #0B0E14 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR NAV
# ---------------------------
st.sidebar.markdown("### NAVIGATION")

if st.sidebar.button("🏠 Accueil"):
    st.session_state.page = "Accueil"

if st.sidebar.button("⚙️ Gestion Maintenance"):
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
        if st.button("GESTION MAINTENANCE"):
            st.session_state.page = "Maintenance"
            st.rerun()

# ---------------------------
# PAGE MAINTENANCE
# ---------------------------
elif st.session_state.page == "Maintenance":

    st.title("Gestion Maintenance")

    # -------- SUB MENU (comme ton screen)
    col_menu, col_content = st.columns([1, 4])

    with col_menu:
        st.markdown("### Navigation")

        if st.button("📊 Tableau de bord"):
            st.session_state.maintenance_tab = "dashboard"

        if st.button("📅 Calendrier"):
            st.session_state.maintenance_tab = "calendar"

        if st.button("✔️ Contrôle périodique"):
            st.session_state.maintenance_tab = "control"

        if st.button("⏱️ Compteurs"):
            st.session_state.maintenance_tab = "counters"

        if st.button("👷 Intervenants"):
            st.session_state.maintenance_tab = "intervenants"

        if st.button("🕓 Historique"):
            st.session_state.maintenance_tab = "history"

    # -------- CONTENU
    with col_content:

        tab = st.session_state.maintenance_tab

        # ---------------- DASHBOARD
        if tab == "dashboard":
            st.subheader("Tableau de bord")

            col1, col2, col3 = st.columns(3)

            col1.metric("Équipements", "24")
            col2.metric("Maintenances", "3")
            col3.metric("Alertes", "1")

        # ---------------- CALENDAR
        elif tab == "calendar":
            st.subheader("Calendrier")
            st.info("Calendrier à connecter")

        # ---------------- CONTROL
        elif tab == "control":
            st.subheader("Contrôles périodiques")

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.checkbox("Contrôle journalier")
            st.checkbox("Contrôle hebdomadaire")
            st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- COMPTEURS
        elif tab == "counters":
            st.subheader("Compteurs")

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.number_input("Heures machine", 0, 5000, 1200)
            st.number_input("Cycles", 0, 10000, 350)
            st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- INTERVENANTS (proche de ton screen)
        elif tab == "intervenants":
            st.subheader("Intervenants")

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.text_input("Nom / Libellé")
            st.text_input("Rôle")
            st.text_input("Téléphone")
            st.text_input("Email")

            st.checkbox("Intervenant extérieur")

            st.markdown("Couleur")
            cols = st.columns(10)
            for i in range(10):
                cols[i].markdown("🔘")

            if st.button("Ajouter"):
                st.success("Intervenant ajouté")

            st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- HISTORIQUE
        elif tab == "history":
            st.subheader("Historique")

            st.table({
                "Date": ["17/04/2026"],
                "Action": ["Contrôle effectué"],
                "Intervenant": ["Dupont"]
            })
