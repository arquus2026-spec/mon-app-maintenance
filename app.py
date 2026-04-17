import streamlit as st
from datetime import date

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="ARQUUS - Système de Maintenance",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. STYLE PROFESSIONNEL (CSS) - LA BASE FIGÉE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Roboto', sans-serif;
    }

    .stApp {
        background-color: #0B0E14;
    }

    /* Titre Principal */
    h1 {
        font-weight: 300 !important;
        color: #FFFFFF !important;
        text-align: center;
        letter-spacing: 3px;
        text-transform: uppercase;
        padding-top: 1rem;
        padding-bottom: 0.5rem;
    }

    /* Date */
    .date-text {
        text-align: center;
        color: #5E6772;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 3rem;
    }

    /* Boutons : Style Industriel */
    div.stButton > button {
        width: 100%;
        border-radius: 4px;
        border: 1px solid #2D333B;
        background-color: #161B22;
        color: #ADBAC7;
        padding: 35px 10px;
        font-size: 13px;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.2s ease;
        line-height: 1.5;
    }

    /* Hover */
    div.stButton > button:hover {
        border-color: #E62E2E;
        color: white;
        background-color: #1C2128;
    }
    
    /* Nettoyage interface */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. LOGO ARQUUS EN HAUT À GAUCHE
col_logo, _ = st.columns([1, 4])
with col_logo:
    st.image("https://www.arquus-defense.com/themes/custom/arquus/logo.svg", width=120)

# 4. NAVIGATION LATÉRALE
st.sidebar.markdown("### MODULES")
selection = st.sidebar.radio("Sélectionner une unité :", [
    "Accueil", 
    "Unité Opérateur", 
    "Unité Technicien", 
    "Intervenants Extérieurs",
    "Gestion Maintenance"
])

# 5. LOGIQUE DES PAGES
if selection == "Accueil":
    st.title("Entretien | AIRE DE LAVAGE – ARQUUS")
    aujourdhui = date.today().strftime("%d . %m . %Y")
    st.markdown(f"<p class='date-text'>Date : {aujourdhui}</p>", unsafe_allow_html=True)
    
    col_l, col_main, col_r = st.columns([1, 6, 1])
    with col_main:
        grid_col1, grid_col2 = st.columns(2)
        with grid_col1:
            if st.button("Opérateur"):
                st.info("Accès Opérateur...")
            if st.button("Technicien"):
                st.info("Accès Technicien...")
        with grid_col2:
            if st.button("Intervenants"):
                st.info("Accès Intervenants...")
            if st.button("Gestion maintenance"):
                st.info("Redirection vers Gestion...")

elif selection == "Gestion Maintenance":
    st.title("Gestion Maintenance")
    st.markdown("<p class='date-text'>Administration du système</p>", unsafe_allow_html=True)
    
    # Grille de 6 boutons (3 colonnes x 2 lignes)
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row2_col1, row2_col2, row2_col3 = st.columns(3)

    with row1_col1:
        if st.button("📊\nTableau de bord"):
            st.write("Module Tableau de bord")
            
    with row1_col2:
        if st.button("📅\nCalendrier"):
            st.write("Module Calendrier")
            
    with row1_col3:
        if st.button("🛡️\nContrôle périodique"):
            st.write("Module Contrôles")

    with row2_col1:
        if st.button("⏲️\nCompteurs"):
            st.write("Module Compteurs")
            
    with row2_col2:
        if st.button("👥\nIntervenants"):
            st.write("Module Intervenants")
            
    with row2_col3:
        if st.button("📜\nHistorique"):
            st.write("Module Historique")

    st.markdown("---")
    if st.button("⬅️ Retour au menu"):
        st.write("Utilisez le menu latéral pour naviguer")

elif selection == "Unité Opérateur":
    st.title("Unité Opérateur")
    st.markdown("---")
    st.write("Interface de saisie opérateur.")

else:
    st.title(selection)
    st.write("Module en cours de configuration.")
