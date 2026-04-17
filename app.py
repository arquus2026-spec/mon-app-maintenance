elif selection == "Gestion Maintenance":
    st.title("Gestion Maintenance")
    st.markdown("---")

    # STYLE DES ONGLETS + ICONES (monochrome, cohérent DA)
    st.markdown("""
    <style>
    .tab-label {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .tab-icon {
        width: 14px;
        height: 14px;
        background-color: #ADBAC7;
        display: inline-block;
        border-radius: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

    # CRÉATION DES ONGLETS
    tabs = st.tabs([
        "📊 Tableau de bord",
        "📅 Calendrier",
        "✔️ Contrôles périodiques",
        "⏱️ Compteurs",
        "👷 Intervenants",
        "🕓 Historique"
    ])

    # CONTENU DES ONGLETS

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
        st.info("Module calendrier à connecter (FullCalendar ou autre).")

    # 3. CONTRÔLES PÉRIODIQUES
    with tabs[2]:
        st.subheader("Contrôles périodiques")
        st.write("Liste des contrôles réglementaires et techniques.")

        st.checkbox("Nettoyage filtres")
        st.checkbox("Inspection visuelle")
        st.checkbox("Contrôle pression")

    # 4. COMPTEURS
    with tabs[3]:
        st.subheader("Compteurs")
        st.write("Suivi des heures et cycles machines.")

        st.number_input("Heures de fonctionnement", value=1200)
        st.number_input("Cycles effectués", value=350)

    # 5. INTERVENANTS
    with tabs[4]:
        st.subheader("Intervenants")
        st.write("Gestion des techniciens et prestataires.")

        st.text_input("Nom intervenant")
        st.selectbox("Type", ["Technicien interne", "Prestataire externe"])

        if st.button("Ajouter intervenant"):
            st.success("Intervenant ajouté.")

    # 6. HISTORIQUE
    with tabs[5]:
        st.subheader("Historique")
        st.write("Historique des opérations réalisées.")

        st.table({
            "Date": ["01/03/2026", "15/03/2026"],
            "Action": ["Contrôle filtre", "Remplacement pompe"],
            "Intervenant": ["Dupont", "Société X"]
        })
