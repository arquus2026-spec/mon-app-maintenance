import streamlit as st
import pandas as pd

# Configuration de la page (inspiré de ton titre "Entretien | AIRE DE LAVAGE")
st.set_page_config(page_title="Entretien AIRE DE LAVAGE", layout="wide")

st.title("🚜 Entretien | AIRE DE LAVAGE")
st.markdown("---")

# --- SECTION 1 : COMPTEUR D'HEURES (Ton "H1: ALERTE") ---
st.header("⏱️ État du Compteur")
col1, col2 = st.columns([1, 2])

with col1:
    heures = st.number_input("Heures actuelles (Colonne P) :", min_value=0, value=0)

with col2:
    if heures >= 1500:
        st.error("🚨 **MAINTENANCE CRITIQUE** : Remplacer le clapet de retenue")
    elif heures >= 1000:
        st.warning("⚠️ **MAINTENANCE IMPORTANTE** : Changer les joints")
    elif heures >= 250:
        st.info("ℹ️ **MAINTENANCE STANDARD** : Faire la vidange")
    else:
        st.success("✅ État opérationnel - Aucune action requise")

st.markdown("---")

# --- SECTION 2 : FORMULAIRE D'ENTRETIEN (Inspiré de ton tableau HTML) ---
st.header("📝 Rapport d'Entretien")

with st.expander("Ajouter une vérification", expanded=True):
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        date = st.date_input("Date de l'intervention")
        activite = st.selectbox("Type d'activité", [
            "Contrôle de niveau", 
            "Nettoyage filtres", 
            "Vidange", 
            "Remplacement pièces",
            "Autre"
        ])
    
    with col_b:
        frequence = st.text_input("Fréquence (ex: 250h, Hebdo...)")
        intervenant = st.text_input("Intervenant")

    with col_c:
        prix_u = st.number_input("Prix Unitaire (€)", min_value=0.0, format="%.2f")
        quantite = st.number_input("Quantité", min_value=0, value=1)
        total_ligne = prix_u * quantite
        st.metric("Total Ligne", f"{total_ligne:.2f} €")

# --- SECTION 3 : RÉCAPITULATIF (Comme ton tableau final) ---
st.header("📊 Historique & Totaux")

# Simulation d'un tableau de données (dans une vraie app on brancherait une base de données)
data = {
    "Date": [date],
    "Activité": [activite],
    "Fréquence": [frequence],
    "Intervenant": [intervenant],
    "Prix U (€)": [prix_u],
    "Qté": [quantite],
    "Total (€)": [total_ligne]
}

df = pd.DataFrame(data)
st.table(df)

# Calcul du total général (comme dans ton script HTML)
st.subheader(f"💰 Total Général : {total_ligne:.2f} €")

if st.button("Enregistrer le rapport"):
    st.balloons()
    st.success("Rapport enregistré localement (Interface de démo)")
