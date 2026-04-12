import streamlit as st

# =================================================================================
# 1. KNOWLEDGE BASE (Your Original Top Scorer Dictionaries)
# =================================================================================

GP_DATA = {
    "HEART_ATTACK_RED_FLAG": {
        "symptoms": ["chest pain", "pain in arm or jaw", "shortness of breath", "sweating"],
        "triage_question": "Is the chest pain crushing and radiating to your left arm or jaw?",
        "diagnosis": "CRITICAL: Possible Heart Attack.",
        "western_remedy": "CALL EMERGENCY SERVICES IMMEDIATELY.",
    },
    "THE_FLU_TIER2": {
        "symptoms": ["body aches", "fatigue", "high fever", "chills"],
        "triage_question": "Are you having difficulty breathing?",
        "diagnosis": "Possible Influenza (Flu).",
        "western_remedy": "Contact your GP or rest at home for 5-7 days.",
        "traditional_remedy": "Use warm compress, garlic, ginger.",
    },
    "SPRAIN_TIER1": {
        "symptoms": ["sprain", "twisted ankle", "joint pain", "swollen joint"],
        "triage_question": "Can you bear weight on the injured area?",
        "diagnosis": "Mild to Moderate Sprain.",
        "western_remedy": "Use RICE method.",
        "traditional_remedy": "Warm compress, Epsom salt bath.",
    }
}

DERM_DATA = {
    "CELLULITIS_RED_FLAG": {
        "symptoms": ["rapidly spreading redness", "extreme pain", "hot to touch"],
        "triage_question": "Do you have a painful, red skin area with a fever?",
        "diagnosis": "CRITICAL: Possible Cellulitis.",
        "western_remedy": "CALL EMERGENCY SERVICES IMMEDIATELY.",
    },
    "PSORIASIS_TIER2": {
        "symptoms": ["silvery scales", "red patches", "flaky skin"],
        "diagnosis": "Possible Psoriasis or Chronic Eczema.",
        "western_remedy": "Book a Dermatologist appointment.",
        "traditional_remedy": "Oatmeal baths and natural oils.",
    }
}

PSYCH_DATA = {
    "SUICIDE_RED_FLAG": {
        "symptoms": ["suicidal thoughts", "self-harm", "harming myself"],
        "triage_question": "Are you thinking about hurting yourself right now?",
        "diagnosis": "CRITICAL: Immediate Danger.",
        "western_remedy": "CALL EMERGENCY SERVICES OR A CRISIS HOTLINE IMMEDIATELY.",
    },
    "GENERAL_ANXIETY_TIER1": {
        "symptoms": ["anxiety", "stress", "difficulty sleeping"],
        "diagnosis": "General Anxiety Disorder or High Stress.",
        "western_remedy": "Consult a counselor.",
        "traditional_remedy": "Deep-breathing and calming teas.",
    }
}

# =================================================================================
# 2. UI SETUP
# =================================================================================

st.set_page_config(page_title="MediGuide AI", page_icon="🩺")
st.title("🩺 MediGuide AI Triage System")
st.write("---")

# Sidebar Selection
option = st.sidebar.selectbox(
    "Choose Specialist",
    ["Select...", "General Physician (Dr. Vital)", "Dermatologist (Dr. Luminous)", "Psychiatrist (Dr. Insight)"]
)

# =================================================================================
# 3. TRIAGE LOGIC (The "Brain")
# =================================================================================

if option == "Select...":
    st.info("👋 Welcome! Please select a doctor from the sidebar to begin.")
else:
    symptoms = st.text_input(f"Consulting {option}: Describe your symptoms below").lower()

    if symptoms:
        # --- DR. VITAL LOGIC ---
        if "Vital" in option:
            if any(k in symptoms for k in GP_DATA["HEART_ATTACK_RED_FLAG"]["symptoms"]):
                st.error("🚨 EMERGENCY CHECK")
                ans = st.radio(GP_DATA["HEART_ATTACK_RED_FLAG"]["triage_question"], ["Select...", "Yes", "No"])
                if ans == "Yes":
                    st.error(GP_DATA["HEART_ATTACK_RED_FLAG"]["western_remedy"])
            
            elif any(k in symptoms for k in GP_DATA["THE_FLU_TIER2"]["symptoms"]):
                st.success(GP_DATA["THE_FLU_TIER2"]["diagnosis"])
                st.write(f"**Western:** {GP_DATA['THE_FLU_TIER2']['western_remedy']}")
                st.write(f"**Traditional:** {GP_DATA['THE_FLU_TIER2']['traditional_remedy']}")

        # --- DR. LUMINOUS LOGIC ---
        elif "Luminous" in option:
            if any(k in symptoms for k in DERM_DATA["CELLULITIS_RED_FLAG"]["symptoms"]):
                st.error("🚨 EMERGENCY CHECK")
                ans = st.radio(DERM_DATA["CELLULITIS_RED_FLAG"]["triage_question"], ["Select...", "Yes", "No"])
                if ans == "Yes":
                    st.error(DERM_DATA["CELLULITIS_RED_FLAG"]["western_remedy"])
            
            elif any(k in symptoms for k in DERM_DATA["PSORIASIS_TIER2"]["symptoms"]):
                st.success(DERM_DATA["PSORIASIS_TIER2"]["diagnosis"])
                st.write(f"**Traditional:** {DERM_DATA['PSORIASIS_TIER2']['traditional_remedy']}")

        # --- DR. INSIGHT LOGIC ---
        elif "Insight" in option:
            if any(k in symptoms for k in PSYCH_DATA["SUICIDE_RED_FLAG"]["symptoms"]):
                st.error("🚨 EMERGENCY CHECK")
                ans = st.radio(PSYCH_DATA["SUICIDE_RED_FLAG"]["triage_question"], ["Select...", "Yes", "No"])
                if ans == "Yes":
                    st.error(PSYCH_DATA["SUICIDE_RED_FLAG"]["western_remedy"])
            
            elif any(k in symptoms for k in PSYCH_DATA["GENERAL_ANXIETY_TIER1"]["symptoms"]):
                st.success(PSYCH_DATA["GENERAL_ANXIETY_TIER1"]["diagnosis"])
                st.write(f"**Traditional:** {PSYCH_DATA['GENERAL_ANXIETY_TIER1']['traditional_remedy']}")

st.divider()
st.caption("⚠️ **Disclaimer:** For educational purposes only. Always seek professional medical advice for health concerns.")
