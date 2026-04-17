import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Maintenance Préventive", page_icon="🔧")

st.title("🔧 Assistant de Maintenance")
st.write("Entrez le nombre d'heures pour vérifier l'état de la machine.")

# Création de la zone de saisie
heures = st.number_input("Compteur d'heures (Colonne P) :", min_value=0, step=1, value=0)

st.divider()

# Logique des alertes (exactement comme ton besoin)
if heures >= 1500:
    st.error("🚨 **ALERTE 1500h** : Remplacer le clapet de retenue")
    st.info("Priorité : Critique")
elif heures >= 1000:
    st.warning("⚠️ **ALERTE 1000h** : Changer les joints")
    st.info("Priorité : Haute")
elif heures >= 250:
    st.info("ℹ️ **ALERTE 250h** : Il faut faire la vidange")
    st.info("Priorité : Standard")
else:
    st.success("✅ **RAS** : Aucune maintenance immédiate requise.")

# Petit tableau récapitulatif en bas
with st.expander("Voir les paliers de maintenance"):
    st.write("- **250h** : Vidange")
    st.write("- **1000h** : Joints")
    st.write("- **1500h** : Clapet de retenue")
