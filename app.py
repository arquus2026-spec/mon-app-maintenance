import streamlit as st
from datetime import date

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="ARQUUS - Système de Maintenance",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. STYLE PROFESSIONNEL (CSS)
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
        padding-bottom: 0.5rem;
    }

    .date-text {
        text-align: center;
        color: #5E6772;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 4rem;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 4px;
        border: 1px solid #2D333B;
        background-color: #161B22;
        color: #ADBAC7;
        padding: 30px 10px;
        font-size: 14px;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        border-color: #E62E2E;
        color: white;
        background-color: #1C2128;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. NAVIGATION LATÉRALE
st.sidebar.markdown("### MODULES")
selection = st.sidebar.radio("Sélectionner une unité :", [
    "Accueil", 
    "Unité Opérateur", 
    "Unité Technicien", 
    "Intervenants Extérieurs",
    "Gestion Maintenance"
])

# 4. LOGIQUE DES PAGES
if selection == "Accueil":
    st.title("Entretien | AIRE DE LAVAGE – ARQUUS")
    
    aujourdhui = date.today().strftime("%d . %m . %Y")
    st.markdown(f"<p class='date-text'>Date : {aujourdhui}</p>", unsafe_allow_html=True)
    
    col_l, col_main, col_r = st.columns([1, 6, 1])

    with col_main:
        grid_col1, grid_col2 = st.columns(2)
        
        with grid_col1:
            if st.button("Opérateur"):
                st.info("Chargement du module Opérateur...")
            
            if st.button("Technicien"):
                st.info("Chargement du module Technicien...")

        with grid_col2:
            if st.button("Intervenants"):
                st.info("Chargement du module Intervenants...")
                
            if st.button("Gestion maintenance"):
                st.info("Chargement du module Gestion...")

elif selection == "Unité Opérateur":
    st.title("Unité Opérateur")
    st.markdown("---")
    st.write("Interface de saisie des données d'exploitation.")
    if st.button("Retour au menu principal"):
        st.rerun()

elif selection == "Gestion Maintenance":
    st.title("Gestion Maintenance")
    st.markdown("---")

    # ONGLET PRINCIPAL
    tabs = st.tabs([
        "📊 Tableau de bord",
        "📅 Calendrier",
        "✔️ Contrôles périodiques",
        "⏱️ Compteurs",
        "👷 Intervenants",
        "🕓 Historique"
    ])

    # 1. TABLEAU DE BORD
    with tabs[0]:
        st.subheader("Tableau de bord")
        st.write("Vue globale de l'état de la maintenance.")

        col1, col2, col3 = st.columns(3)
        col1.metric("Équipements actifs", "24")
        col2.metric("Maintenances en cours", "3")
        col3.metric("Alertes", "1", delta="-1")

    # 2. CALENDRIER
    with tabs[1]:
        st.subheader("Calendrier")
        st.write("Planification des interventions.")
        st.info("Module calendrier à connecter.")

    # 3. CONTRÔLES PÉRIODIQUES
    with tabs[2]:
        st.subheader("Contrôles périodiques")
        st.write("Liste des contrôles techniques.")

        st.checkbox("Nettoyage filtres")
        st.checkbox("Inspection visuelle")
        st.checkbox("Contrôle pression")

    # 4. COMPTEURS
    with tabs[3]:
        st.subheader("Compteurs")
        st.write("Suivi des compteurs machines.")

        heures = st.number_input("Heures de fonctionnement", value=1200)
        cycles = st.number_input("Cycles effectués", value=350)

        st.write(f"Heures : {heures} | Cycles : {cycles}")

    # 5. INTERVENANTS
    with tabs[4]:
        st.subheader("Intervenants")
        st.write("Gestion des intervenants.")

        nom = st.text_input("Nom intervenant")
        type_interv = st.selectbox("Type", ["Technicien interne", "Prestataire externe"])

        if st.button("Ajouter intervenant"):
            st.success(f"{nom} ajouté ({type_interv})")

    # 6. HISTORIQUE
    with tabs[5]:
        st.subheader("Historique")
        st.write("Historique des opérations.")

        st.table({
            "Date": ["01/03/2026", "15/03/2026"],
            "Action": ["Contrôle filtre", "Remplacement pompe"],
            "Intervenant": ["Dupont", "Société X"]
        })

else:
    st.title(selection)
    st.write("Module en cours de configuration.")
