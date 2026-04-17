import streamlit as st
from datetime import date

# 1. CONFIGURATION DE LA PAGE (Mode sombre et titre)
st.set_page_config(
    page_title="ARQUUS - Gestion de Maintenance",
    page_icon=" I ",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. STYLE PERSONNALISÉ (Pour forcer l'aspect sombre et le design)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    h1 {
        color: #ffffff;
        text-align: center;
        border-bottom: 2px solid #ff4b4b;
        padding-bottom: 10px;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        background-color: #262730;
        color: white;
        border: 1px solid #464646;
    }
    .stButton>button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRE LATÉRALE (MENU DE NAVIGATION)
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Aller vers :", [
    "Accueil", 
    "Entretien Aire de Lavage", 
    "Historique des Données", 
    "Paramètres"
])

# 4. LOGIQUE DES PAGES
if selection == "Accueil":
    # Titre principal
    st.title("GESTION DE MAINTENANCE")
    
    # Affichage de la date (comme demandé)
    aujourdhui = date.today().strftime("%d/%m/%Y")
    st.markdown(f"<h3 style='text-align: center; color: #aaaaaa;'>Date du jour : {aujourdhui}</h3>", unsafe_allow_html=True)
    
    st.write("##") # Espace

    # Création des 4 boutons/pages (en colonnes)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("ENTRETIEN"):
            st.info("Page d'entretien en cours de création...")
        
        if st.button("STATISTIQUES"):
            st.info("Page de statistiques en cours de création...")

    with col2:
        if st.button("RAPPORTS"):
            st.info("Page de rapports en cours de création...")
            
        if st.button("ALERTES"):
            st.info("Page d'alertes en cours de création...")

elif selection == "Entretien Aire de Lavage":
    st.title("Entretien Aire de Lavage")
    st.write("C'est ici que nous mettrons ton tableau de maintenance plus tard.")
    if st.button("Retour à l'accueil"):
        st.write("Utilisez le menu à gauche pour revenir.")

else:
    st.title(selection)
    st.write(f"Le contenu de la page '{selection}' sera ajouté aux étapes suivantes.")
