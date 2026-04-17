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



    /* Titre Principal : sobre et élégant */

    h1 {

        font-weight: 300 !important;

        color: #FFFFFF !important;

        text-align: center;

        letter-spacing: 3px;

        text-transform: uppercase;

        padding-top: 2rem;

        padding-bottom: 0.5rem;

    }



    /* Date : discrète et technique */

    .date-text {

        text-align: center;

        color: #5E6772;

        font-size: 0.9rem;

        text-transform: uppercase;

        letter-spacing: 1px;

        margin-bottom: 4rem;

    }



    /* Boutons : Style "Flat UI" industriel */

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



    /* Hover : changement de couleur subtil vers le rouge ARQUUS */

    div.stButton > button:hover {

        border-color: #E62E2E;

        color: white;

        background-color: #1C2128;

    }

    

    /* Nettoyage de l'interface Streamlit */

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

    # En-tête

    st.title("Entretien | AIRE DE LAVAGE – ARQUUS")

    

    # Date formatée professionnellement

    aujourdhui = date.today().strftime("%d . %m . %Y")

    st.markdown(f"<p class='date-text'>Date : {aujourdhui}</p>", unsafe_allow_html=True)

    

    # Structure de la grille de navigation

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

                

            if st.button("Gestion"):

                st.info("Chargement du module Gestion...")



elif selection == "Unité Opérateur":

    st.title("Unité Opérateur")

    st.markdown("---")

    st.write("Interface de saisie des données d'exploitation.")

    if st.button("Retour au menu principal"):

        st.rerun()



else:

    st.title(selection)

    st.write("Module en cours de configuration.")
