
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

        # Step 3: Standard Care (The "Treatment Plan")
        st.subheader("📋 Your Personalized Care Plan")
        
        # Logic to find the non-emergency match...
        # If match found (e.g., Common Cold):
        st.write("### Analysis: Common
