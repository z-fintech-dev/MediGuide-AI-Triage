
import streamlit as st

# =============================================================
# 1. THE DATA (Your original "Brain")
# =============================================================
# [Include your full GP_DATA, DERM_DATA, and PSYCH_DATA here]

# =============================================================
# 2. UI SETTINGS
# =============================================================
st.set_page_config(page_title="MediGuide AI", page_icon="🩺")
st.title("🩺 MediGuide AI: Professional Triage")

# Treatment Preference - Solves the "Automatic Remedy" mishap
preference = st.sidebar.radio(
    "Treatment Preference:",
    ["Integrated (Both)", "Western / Clinical 💊", "Traditional / Natural 🌿"]
)

option = st.sidebar.selectbox(
    "Select Specialist:",
    ["Select...", "General Physician", "Dermatologist", "Psychiatrist"]
)

# =============================================================
# 3. THE SMART FLOW
# =============================================================

if option != "Select...":
    symptoms = st.text_input("Describe your symptoms accurately:").lower()

    if symptoms:
        # Step 1: Check for Red Flags (Silent Scan)
        is_emergency = False
        target_data = {}
        
        # Example for GP logic (Apply this pattern to all)
        if option == "General Physician":
            if any(k in symptoms for k in ["chest pain", "shortness of breath"]):
                target_data = {
                    "q": "Is the pain crushing or radiating to your arm?",
                    "diag": "Possible Heart Attack",
                    "west": "CALL 911/999 IMMEDIATELY",
                    "trad": "Seek emergency care immediately."
                }
                is_emergency = True
        
        # Step 2: Handle Emergency Logic
        if is_emergency:
            st.error("🚨 CRITICAL CHECK REQUIRED")
            ans = st.radio(target_data["q"], ["Select...", "Yes", "No"])
            
            if ans == "Yes":
                st.error(f"**URGENT:** {target_data['west']}")
                st.stop() # Stop here for safety
            elif ans == "No":
                st.success("✅ Emergency ruled out. Proceeding to standard care...")
                # The code will now naturally continue to the next part!

       # =============================================================
        # Step 3: Standard Care (The "Search Engine")
        # =============================================================
        st.subheader("📋 Your Personalized Care Plan")
        
        found_condition = None
        current_db = {}

        # 1. Identify which doctor's data to search
        if "Vital" in option:
            current_db = GP_DATA
        elif "Luminous" in option:
            current_db = DERM_DATA
        elif "Insight" in option:
            current_db = PSYCH_DATA

        # 2. Search for the keyword match in the correct dictionary
        for condition_key, data in current_db.items():
            if any(symptom in symptoms for symptom in data["symptoms"]):
                found_condition = data
                # Displays the name of the condition nicely (e.g., Common Cold)
                st.markdown(f"### Analysis: {condition_key.replace('_', ' ').title()}")
                break

        # 3. Display the REAL data in the columns
        if found_condition:
            col1, col2 = st.columns(2)
            
            if preference in ["Integrated (Both)", "Western / Clinical 💊"]:
                with col1:
                    st.info("**Western Remedy**")
                    st.write(found_condition.get("western_remedy", "Contact your GP for details."))
            
            if preference in ["Integrated (Both)", "Traditional / Natural 🌿"]:
                with col2:
                    st.success("**Traditional Remedy**")
                    st.write(found_condition.get("traditional_remedy", "No specific natural remedy listed."))
        else:
            st.warning("No specific match found. Please describe your symptoms differently or consult a professional.")
