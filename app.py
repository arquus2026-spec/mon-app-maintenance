import streamlit as st
from datetime import date

# ---------------------------
# INIT NAVIGATION
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

# ---------------------------
# CONFIG PAGE
# ---------------------------
st.set_page_config(
    page_title="ARQUUS - Système de Maintenance",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------
# STYLE
# ---------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

html, body, [class*="st-"] {
    font-family: 'Roboto', sans-serif;
}

.stApp {
    background-color: #0B0E14;
}

h1 {
    font-weight: 300 !important;
    color: #FFFFFF !important;
    text-align: center;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding-top: 2rem;
}

.date-text {
    text-align: center;
    color: #5E6772;
    font-size: 0.9rem;
    letter-spacing: 1px;
    margin-bottom: 3rem;
}

div.stButton > button {
    width: 100%;
    border-radius: 4px;
    border: 1px solid #2D333B;
    background-color: #161B22;
    color: #ADBAC7;
    padding: 30px 10px;
    text-transform: uppercase;
    transition: 0.2s;
}

div.stButton > button:hover {
    border-color: #E62E2E;
    color: white;
}

#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.markdown("### MODULES")

if st.sidebar.button("Accueil"):
    st.session_state.page = "Accueil"

if st.sidebar.button("Unité Opérateur"):
    st.session_state.page = "Opérateur"

if st.sidebar.button("Gestion Maintenance"):
    st.session_state.page = "Maintenance"

# ---------------------------
# ROUTER
# ---------------------------
page = st.session_state.page

# ---------------------------
# ACCUEIL
# ---------------------------
if page == "Accueil":
    st.title("Entretien | AIRE DE LAVAGE – ARQUUS")

    aujourdhui = date.today().strftime("%d . %m . %Y")
    st.markdown(f"<p class='date-text'>Date : {aujourdhui}</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Opérateur"):
            st.session_state.page = "Opérateur"
            st.rerun()

    with col2:
        if st.button("Gestion maintenance"):
            st.session_state.page = "Maintenance"
            st.rerun()

# ---------------------------
# OPÉRATEUR
# ---------------------------
elif page == "Opérateur":
    st.title("Unité Opérateur")
    st.write("Interface opérateur")

    if st.button("Retour"):
        st.session_state.page = "Accueil"
        st.rerun()

# ---------------------------
# MAINTENANCE
# ---------------------------
elif page == "Maintenance":
    st.title("Gestion Maintenance")
    st.markdown("---")

    tabs = st.tabs([
        "📊 Tableau de bord",
        "📅 Calendrier",
        "✔️ Contrôles",
        "⏱️ Compteurs",
        "👷 Intervenants",
        "🕓 Historique"
    ])

    # TAB 1
    with tabs[0]:
        st.subheader("Tableau de bord")
        col1, col2, col3 = st.columns(3)
        col1.metric("Machines", "24")
        col2.metric("Maintenances", "3")
        col3.metric("Alertes", "1")

    # TAB 2
    with tabs[1]:
        st.subheader("Calendrier")
        st.info("À connecter")

    # TAB 3
    with tabs[2]:
        st.checkbox("Contrôle filtre")
        st.checkbox("Inspection")

    # TAB 4
    with tabs[3]:
        st.number_input("Heures", 0, 5000, 1200)

    # TAB 5
    with tabs[4]:
        nom = st.text_input("Nom")
        if st.button("Ajouter"):
            st.success(f"{nom} ajouté")

    # TAB 6
    with tabs[5]:
        st.table({
            "Date": ["01/03"],
            "Action": ["Contrôle"]
        })

    if st.button("Retour accueil"):
        st.session_state.page = "Accueil"
        st.rerun()
