
import streamlit as st

# =============================================================
# 1. THE DATA (Your original "Brain")
# =============================================================
## =================================================================================
# 1. KNOWLEDGE BASE (DICTIONARIES)
# =================================================================================

# ---------------------------------------------------------------------------------
# GENERAL PHYSICIAN DATA (GP_DATA)
# ---------------------------------------------------------------------------------
GP_DATA = {
    # TIER 3: Red Flag (Emergency Stop)
    "HEART_ATTACK_RED_FLAG": {
        "symptoms": ["chest pain", "pain in arm or jaw", "shortness of breath", "sweating"],
        "triage_question": "Is the chest pain crushing and radiating to your left arm or jaw (Y/N)?",
        "diagnosis": "CRITICAL: Possible Heart Attack.",
        "western_remedy": "CALL EMERGENCY SERVICES (e.g., 999 or 911) IMMEDIATELY.",
        "traditional_remedy": "CALL EMERGENCY SERVICES IMMEDIATELY.",
        "stop_warning": True
    },

    # TIER 2: Moderate Issue (Pharmacy/GP Appointment)
    "THE_FLU_TIER2": {
        "symptoms": ["body aches", "fatigue", "high fever", "chills"],
        "triage_question": "Are you having difficulty breathing or shortness of breath (Y/N)?",
        "diagnosis": "Possible Influenza (Flu).",
        "western_remedy": "Contact your GP for an antiviral prescription or rest at home for 5-7 days.",
        "traditional_remedy": "Use a warm compress, consume immunity-boosting foods like garlic and ginger.",
        "stop_warning": False
    },
# TIER 1/2: Depending on severity.
    "SPRAIN_TIER1": {
        "symptoms": ["sprain", "twisted ankle", "joint pain", "swollen joint"],
        "triage_question": "Can you bear *any* weight on the injured area, even lightly (Y/N)?",
        "diagnosis": "Mild to Moderate Sprain.",
        "western_remedy": "Follow the R.I.C.E. method: Rest, Ice (for 20 min every 2-3 hours), Compression (bandage), and Elevation. Take OTC pain relievers (like ibuprofen) for pain and swelling.",
        "traditional_remedy": "Apply a warm compress (after the first 48 hours), use Epsom salt baths to soak the joint, and gently massage with a soothing herbal oil.",
        "stop_warning": False
    },

    # TIER 1: Minor.
    "HEADACHE_TIER1": {
        "symptoms": ["headache", "dull ache", "head tension", "pain in temples"],
        "triage_question": "Do you also have blurred vision, fever, or pain when bending your head to your chest (Y/N)?",
        "diagnosis": "Tension Headache.",
        "western_remedy": "Take an over-the-counter pain reliever (like acetaminophen or ibuprofen). Ensure you are well-hydrated and avoid bright screens for a short time.",
        "traditional_remedy": "Apply a cold or warm compress to the temples or neck. Use peppermint or lavender oil on the temples and practice deep, slow breathing exercises.",
        "stop_warning": False
    },
    
    # TIER 1: Minor Issue (Home Remedy)
    "COMMON_COLD_TIER1": {
        "symptoms": ["runny nose", "sore throat", "sneezing", "headache"],
        "triage_question": "Do you have a temperature of 102°F (38.9°C) or higher (Y/N)?",
        "diagnosis": "Common Cold.",
        "western_remedy": "Rest, fluids, and over-the-counter pain relievers like paracetamol.",
        "traditional_remedy": "Drink warm lemon and honey tea, steam inhalation.",
        "stop_warning": False
    }
}

# ---------------------------------------------------------------------------------
# DERMATOLOGIST DATA (DERM_DATA)
# ---------------------------------------------------------------------------------
DERM_DATA = {
    # TIER 3: Red Flag (Emergency Stop) - A Severe Infection
    "CELLULITIS_RED_FLAG": {
        "symptoms": ["rapidly spreading redness", "extreme pain", "skin hot to touch", "fever"],
        "triage_question": "Do you have a spreading area of hot, painful, red skin accompanied by a fever over 100.4°F (38°C) (Y/N)?",
        "diagnosis": "CRITICAL: Possible Cellulitis (Severe Skin Infection).",
        "western_remedy": "CALL EMERGENCY SERVICES (e.g., 999 or 911) IMMEDIATELY, as this can lead to sepsis.",
        "traditional_remedy": "CALL EMERGENCY SERVICES IMMEDIATELY. This infection requires urgent antibiotics.",
        "stop_warning": True
    },

    # TIER 2: Moderate Issue (Dermatologist Appointment) - Chronic Condition
    "PSORIASIS_TIER2": {
        "symptoms": ["thick silvery scales", "red patches", "flaky skin", "joint stiffness"],
        "triage_question": "Is the skin condition causing you difficulty walking, significant joint pain, or preventing sleep (Y/N)?",
        "diagnosis": "Possible Psoriasis or Chronic Eczema.",
        "western_remedy": "Book a routine appointment with a Dermatologist or GP for prescription medication and management plan.",
        "traditional_remedy": "Use moisturizing creams with natural oils (coconut, olive). Avoid alcohol and inflammatory foods. Take warm oatmeal baths.",
        "stop_warning": False
    },
# TIER 1: Minor Issue (Home Remedy) - Minor Irritation
    "CONTACT_DERMATITIS_TIER1": {
        "symptoms": ["itchy rash", "small bumps", "skin irritation", "redness in patches"],
        "triage_question": "Is the rash located only where your skin touched a specific irritant (e.g., jewelry, plant, new soap) (Y/N)?",
        "diagnosis": "Contact Dermatitis (Minor Rash).",
        "western_remedy": "Avoid the irritant. Apply an over-the-counter hydrocortisone cream and a cooling anti-itch lotion (like Calamine).",
        "traditional_remedy": "Apply a cool compress or a poultice made from chamomile or witch hazel to soothe the inflammation.",
        "stop_warning": False
    }
}
# ---------------------------------------------------------------------------------
# PSYCHIATRIST DATA (PSYCH_DATA)
# ---------------------------------------------------------------------------------
PSYCH_DATA = {
    # TIER 3: Red Flag (Emergency Stop) - Suicide.
    "SUICIDE_RED_FLAG": {
        "symptoms": ["suicidal thoughts", "self-harm", "harming myself", "killing myself", "ending my life"],
        "triage_question": "Are you thinking about ending your life or planning to hurt yourself right now (Y/N)?",
        "diagnosis": "CRITICAL: Immediate Danger to Self.",
        "western_remedy": "CALL EMERGENCY SERVICES (e.g., 999 or 911) or a local crisis hotline IMMEDIATELY. Do not wait. Talk to someone now.",
        "traditional_remedy": "CALL EMERGENCY SERVICES or a local crisis hotline IMMEDIATELY. Find a safe place and talk to a trusted adult.",
        "stop_warning": True
    },

    # TIER 2: Moderate Issue (Urgent Consultation) - Severe Depression.
    "SEVERE_DEPRESSION_TIER2": {
        "symptoms": ["severe depression", "panic attack", "bipolar episode", "lost interest in everything", "sleeping all day"],
        "triage_question": "Have these feelings made it impossible for you to go to work/school or get out of bed for three or more days (Y/N)?",
        "diagnosis": "Severe Depression or Panic/Mood Disorder.",
        "western_remedy": "It is important to seek professional help this week. Contact a Psychiatrist or Psychologist for a full evaluation and treatment plan.",
        "traditional_remedy": "Seek professional help immediately. Focus on small steps: drink water, sit outside for 5 minutes, and call a friend or family member for support.",
        "stop_warning": False
    },

    # TIER 1: Minor Issue (General Consultation) - General Anxiety.
    "GENERAL_ANXIETY_TIER1": {
        "symptoms": ["general anxiety", "social phobia", "difficulty sleeping", "stress", "feeling worried all the time"],
        "triage_question": "Do you feel completely overwhelmed by everyday life or has this anxiety been constant for more than one month (Y/N)?",
        "diagnosis": "General Anxiety Disorder or High Stress.",
        "western_remedy": "Consider booking a consultation with a counselor or therapist. Practice mindfulness and try to establish a regular sleep schedule.",
        "traditional_remedy": "Practice deep-breathing exercises. Drink calming teas (like Chamomile or Lavender). Engage in mild physical activity to reduce tension.",
        "stop_warning": False
    }
}

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

      
     # --- START OF STEP 3: FLEXIBLE SEARCH ---
        found_condition = None
        
        # 1. Ensure current_db is always defined to prevent NameError
        current_db = {} 

        # 2. Match the exact text from your sidebar selectbox
        if option == "General Physician":
            current_db = GP_DATA
        elif option == "Dermatologist":
            current_db = DERM_DATA
        elif option == "Psychiatrist":
            current_db = PSYCH_DATA
        
        # 3. Only run the loop if current_db actually has data
        if current_db:
            for condition_key, data in current_db.items():
                # Skip the emergency one if we already cleared it
                if is_emergency and "RED_FLAG" in condition_key:
                    continue 
                    
                for keyword in data["symptoms"]:
                    if keyword.lower() in symptoms.lower():
                        found_condition = data
                        condition_name = condition_key.replace('_', ' ').title()
                        break
                if found_condition:
                    break
                
        # --- STEP 4: DISPLAYING THE RESULTS ---
        if found_condition:
            st.markdown(f"### Analysis: {condition_name}")
            col1, col2 = st.columns(2)
            
            if preference in ["Integrated (Both)", "Western / Clinical 💊"]:
                with col1:
                    st.info("**Western Remedy**")
                    st.write(found_condition.get("western_remedy"))
            
            if preference in ["Integrated (Both)", "Traditional / Natural 🌿"]:
                with col2:
                    st.success("**Traditional Remedy**")
                    st.write(found_condition.get("traditional_remedy"))
        else:
            st.warning("No specific match found. Try using simpler words like 'fever' or 'cough'.")

        
