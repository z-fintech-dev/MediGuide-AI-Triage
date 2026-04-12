#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# =================================================================================
# 2. TRIAGE FUNCTIONS (The Logic)
# =================================================================================

# ---------------------------------------------------------------------------------
# GENERAL PHYSICIAN TRIAGE
# ---------------------------------------------------------------------------------
def run_gp_triage():
    """Simulates the General Physician's triage process based on symptoms."""
    print("\n👋 Welcome to Dr. Vital's (The Triage Master) office")
    print("I can help you with common ailments, but I must screen for emergencies first.")
    
    # Get the user initial symptoms.
    user_symptoms_raw = input("Please describe your main symptoms (e.g., sore throat, chest pain, high fever, headache, sprain): ").lower()
    
    # ----------------------------------------------------------------
    # 1. CHECK FOR EMERGENCY (Heart Attack Red Flag) - TIER 3
    # ----------------------------------------------------------------
    if any(keyword in user_symptoms_raw for keyword in GP_DATA["HEART_ATTACK_RED_FLAG"]["symptoms"]):
        
        red_flag_answer = input(GP_DATA["HEART_ATTACK_RED_FLAG"]["triage_question"] + " ").upper()
        
        if red_flag_answer == 'Y':
            print("\n🚨 **CRITICAL EMERGENCY ALERT** 🚨")
            print(f"Diagnosis: {GP_DATA['HEART_ATTACK_RED_FLAG']['diagnosis']}")
            print("---")
            print(f"Action: {GP_DATA['HEART_ATTACK_RED_FLAG']['western_remedy']}")
            return # Immediate exit
        else:
            print("Thank you. Moving to less urgent checks.")

    # ----------------------------------------------------------------
    # 2. CHECK FOR SPRAIN (Tier 1/2)
    # ----------------------------------------------------------------
    elif any(keyword in user_symptoms_raw for keyword in GP_DATA["SPRAIN_TIER1"]["symptoms"]):
        
        sprain_answer = input(GP_DATA["SPRAIN_TIER1"]["triage_question"] + " ").upper()
        
        print("\n--- MediGuide Recommendation (Dr. Vital) ---")
        if sprain_answer == 'N':
            print("🚨 **HIGH URGENCY:** Since you cannot bear weight, this could be a fracture or severe tear. See an Urgent Care facility for an X-ray immediately.")
            return
        else:
            print(f"Diagnosis: {GP_DATA['SPRAIN_TIER1']['diagnosis']}")
            print("Action (Western): " + GP_DATA["SPRAIN_TIER1"]["western_remedy"])
            print("Action (Traditional): " + GP_DATA["SPRAIN_TIER1"]["traditional_remedy"])
            return

    # ----------------------------------------------------------------
    # 3. CHECK FOR MODERATE ISSUE (The Flu) - TIER 2
    # ----------------------------------------------------------------
    elif any(keyword in user_symptoms_raw for keyword in GP_DATA["THE_FLU_TIER2"]["symptoms"]):

        flu_answer = input(GP_DATA["THE_FLU_TIER2"]["triage_question"] + " ").upper()

        print("\n--- MediGuide Recommendation (Dr. Vital) ---")
        if flu_answer == 'Y':
            print("⚠️ **MODERATE URGENCY:** Contact your GP or go to an urgent care facility immediately. Difficulty breathing is a serious symptom.")
            return
        else:
            print(f"Diagnosis: {GP_DATA['THE_FLU_TIER2']['diagnosis']}")
            print("Action (Western): " + GP_DATA["THE_FLU_TIER2"]["western_remedy"])
            print("Action (Traditional): " + GP_DATA["THE_FLU_TIER2"]["traditional_remedy"])
            return

    # ----------------------------------------------------------------
    # 4. CHECK FOR HEADACHE (Tier 1)
    # ----------------------------------------------------------------
    elif any(keyword in user_symptoms_raw for keyword in GP_DATA["HEADACHE_TIER1"]["symptoms"]):
        
        headache_answer = input(GP_DATA["HEADACHE_TIER1"]["triage_question"] + " ").upper()
        
        print("\n--- MediGuide Recommendation (Dr. Vital) ---")
        if headache_answer == 'Y':
            print("⚠️ **MODERATE URGENCY:** Your symptoms (blurred vision/fever) could indicate a severe migraine or infection. Please contact your GP's office today.")
            return
        else:
            print(f"Diagnosis: {GP_DATA['HEADACHE_TIER1']['diagnosis']}")
            print("Action (Western): " + GP_DATA["HEADACHE_TIER1"]["western_remedy"])
            print("Action (Traditional): " + GP_DATA["HEADACHE_TIER1"]["traditional_remedy"])
            return

    # ----------------------------------------------------------------
    # 5. CHECK FOR MINOR ISSUE (Common Cold) - TIER 1
    # ----------------------------------------------------------------
    elif any(keyword in user_symptoms_raw for keyword in GP_DATA["COMMON_COLD_TIER1"]["symptoms"]):
        
        cold_answer = input(GP_DATA["COMMON_COLD_TIER1"]["triage_question"] + " ").upper()
        
        print("\n--- MediGuide Recommendation (Dr. Vital) ---")
        if cold_answer == 'Y':
            print("⚠️ **MODERATE URGENCY:** If your fever is high, it's likely the flu or a more serious infection. Contact your GP.")
            return
        else:
            print(f"Diagnosis: {GP_DATA['COMMON_COLD_TIER1']['diagnosis']}")
            print("Action (Western): " + GP_DATA["COMMON_COLD_TIER1"]["western_remedy"])
            print("Action (Traditional): " + GP_DATA["COMMON_COLD_TIER1"]["traditional_remedy"])
            return

    # ----------------------------------------------------------------
    # 6. DEFAULT/UNKNOWN RESPONSE
    # ----------------------------------------------------------------
    else:
        print("\n🤔 Sorry, I do not have a specific triage path for those exact symptoms.")
        print("Recommendation: Since no critical red flags were mentioned, book a routine appointment with your local General Physician for a check-up.")

# ---------------------------------------------------------------------------------
# DERMATOLOGIST TRIAGE
# ---------------------------------------------------------------------------------
def run_derm_triage():
    """Simulates the dermatologist's triage system based on symptoms."""
    print("\n👋 Welcome to Dr. Luminous's (The Triage Master) office")
    print("I can help you with common ailments, but I must screen for emergencies first.")
    
    user_symptoms_raw = input("Please describe your main symptoms (e.g., rapidly spreading redness, flaky skin, itchy rash): ").lower()
    
    # ----------------------------------------------------------------
    # 1. CHECK FOR EMERGENCY (Cellulitis Red Flag) - TIER 3
    # ----------------------------------------------------------------
    if any(keyword in user_symptoms_raw for keyword in DERM_DATA["CELLULITIS_RED_FLAG"]["symptoms"]):
        
        red_flag_answer = input(DERM_DATA["CELLULITIS_RED_FLAG"]["triage_question"] + " ").upper()

        if red_flag_answer == 'Y':
            print("\n🚨 **CRITICAL EMERGENCY ALERT** 🚨")
            print(f"Diagnosis: {DERM_DATA['CELLULITIS_RED_FLAG']['diagnosis']}")
            print("---")
            print(f"Action: {DERM_DATA['CELLULITIS_RED_FLAG']['western_remedy']}")
            return # Immediate exit

        else:
            print("Thank you. Moving to less urgent checks.")

    # ----------------------------------------------------------------
    # 2. CHECK FOR MODERATE ISSUE (Chronic condition - Psoriasis) - TIER 2
    # ----------------------------------------------------------------
    elif any(keyword in user_symptoms_raw for keyword in DERM_DATA["PSORIASIS_TIER2"]["symptoms"]):
        
        psoriasis_answer = input(DERM_DATA["PSORIASIS_TIER2"]["triage_question"] + " ").upper()
        
        print("\n--- MediGuide Recommendation (Dr. Luminous) ---")
        if psoriasis_answer == 'Y':
            print("⚠️ **MODERATE URGENCY:** Your symptoms are significantly impacting your life. Please book a specialist Dermatologist appointment soon for comprehensive treatment.")
            print("Diagnosis: " + DERM_DATA["PSORIASIS_TIER2"]["diagnosis"])
            return
        else:
            print(f"Diagnosis: {DERM_DATA['PSORIASIS_TIER2']['diagnosis']}")
            print("Action (Western): " + DERM_DATA["PSORIASIS_TIER2"]["western_remedy"])
            print("Action (Traditional): " + DERM_DATA["PSORIASIS_TIER2"]["traditional_remedy"])
            return

    # ----------------------------------------------------------------
    # 3. CHECK FOR MINOR ISSUE (Contact Dermatitis) - TIER 1
    # ----------------------------------------------------------------
    elif any(keyword in user_symptoms_raw for keyword in DERM_DATA["CONTACT_DERMATITIS_TIER1"]["symptoms"]):

        minor_irritation_answer = input(DERM_DATA["CONTACT_DERMATITIS_TIER1"]['triage_question'] + " ").upper()

        print("\n--- MediGuide Recommendation (Dr. Luminous) ---")
        if minor_irritation_answer == 'Y':
            print(f"Diagnosis: {DERM_DATA['CONTACT_DERMATITIS_TIER1']['diagnosis']}")
            print("Action (Western): " + DERM_DATA['CONTACT_DERMATITIS_TIER1']['western_remedy'])
            print("Action (Traditional): " + DERM_DATA['CONTACT_DERMATITIS_TIER1']['traditional_remedy'])
            return
        else:
            print("Recommendation: ** Moderate Urgency ** The rash is not contact related. It could be serious. Please contact the DERM's office today.")
            return

    # ----------------------------------------------------------------
    # 4. DEFAULT/UNKNOWN RESPONSE
    # ----------------------------------------------------------------
    else:
        print("\n🤔 Sorry, I do not have a specific triage path for those exact symptoms.")
        print("Recommendation: Since no critical red flags were mentioned, book a routine appointment with your local General Physician for a check-up.")

# ---------------------------------------------------------------------------------
# PSYCHIATRIST TRIAGE
# ---------------------------------------------------------------------------------
def run_psych_triage():
    """Simulates the psychiatrist triage based on symptoms."""
    print("\n👋 Welcome to Dr. Insight's (The Triage Master) office")
    print("I can help you with common ailments, but I must screen for emergencies first.")
    
    user_symptoms_raw = input("Please describe your main symptoms (e.g., suicidal thoughts, severe depression, general anxiety): ").lower()
    
    # ----------------------------------------------------------------
    # 1. CHECK FOR EMERGENCY (Suicide) - TIER 3
    # ----------------------------------------------------------------
    if any(keyword in user_symptoms_raw for keyword in PSYCH_DATA["SUICIDE_RED_FLAG"]["symptoms"]):

        suicide_triage_answer = input(PSYCH_DATA['SUICIDE_RED_FLAG']['triage_question'] + " ").upper()

        if suicide_triage_answer == 'Y':
            print("\n🚨 **CRITICAL EMERGENCY ALERT** 🚨")
            print(f"Diagnosis: {PSYCH_DATA['SUICIDE_RED_FLAG']['diagnosis']}")
            print("---")
            print(f"Action: {PSYCH_DATA['SUICIDE_RED_FLAG']['western_remedy']}")
            return # Immediate exit
        else:
            print("Thank you. Moving to less urgent checks.")
            
    # ----------------------------------------------------------------
    # 2. CHECK FOR MODERATE ISSUE (Severe Depression/Panic Disorder) - TIER 2
    # ----------------------------------------------------------------
    elif any(keyword in user_symptoms_raw for keyword in PSYCH_DATA["SEVERE_DEPRESSION_TIER2"]['symptoms']):

        panic_disorder_answer = input(PSYCH_DATA['SEVERE_DEPRESSION_TIER2']['triage_question'] + " ").upper()

        print("\n--- MediGuide Recommendation (Dr. Insight) --- ")
        if panic_disorder_answer == "Y":
            print("⚠️ **MODERATE URGENCY:** Your symptoms are significantly impacting your life. Please book a specialist Psychiatrist appointment soon for comprehensive treatment.")
            print("Diagnosis: " + PSYCH_DATA["SEVERE_DEPRESSION_TIER2"]["diagnosis"])
            return 
        else:
            print(f"Diagnosis: {PSYCH_DATA['SEVERE_DEPRESSION_TIER2']['diagnosis']}" )
            print("Action (Western): " + PSYCH_DATA["SEVERE_DEPRESSION_TIER2"]["western_remedy"])
            print("Action (Traditional): " + PSYCH_DATA["SEVERE_DEPRESSION_TIER2"]["traditional_remedy"])
            return
            
    # ----------------------------------------------------------------
    # 3. CHECK FOR MINOR ISSUE (General Anxiety/Stress) - TIER 1
    # ----------------------------------------------------------------
    elif any(keyword in user_symptoms_raw for keyword in PSYCH_DATA["GENERAL_ANXIETY_TIER1"]['symptoms']):

        stress_answer = input(PSYCH_DATA["GENERAL_ANXIETY_TIER1"]["triage_question"] + " ").upper()

        print("\n--- MediGuide Recommendation (Dr. Insight) --- ")
        if stress_answer == 'Y':
            print("Recommendation: ** Moderate Urgency ** Your anxiety is serious. It's likely a persistent condition. Please contact the PSYCH'S office today.")
            return
        else:
            print(f"Diagnosis: {PSYCH_DATA['GENERAL_ANXIETY_TIER1']['diagnosis']}")
            print("Action (Western): " + PSYCH_DATA['GENERAL_ANXIETY_TIER1']['western_remedy'])
            print("Action (Traditional): " + PSYCH_DATA['GENERAL_ANXIETY_TIER1']['traditional_remedy'])
            return
            
    # ----------------------------------------------------------------
    # 4. DEFAULT/UNKNOWN RESPONSE
    # ----------------------------------------------------------------
    else:
        print("\n🤔 Sorry, I do not have a specific triage path for those exact symptoms.")
        print("Recommendation: Since no critical red flags were mentioned, book a routine appointment with your local General Physician for a check-up.")


# =================================================================================
# 3. MAIN MENU (The Starter)
# =================================================================================

def main_menu():
    """Presents the user with the main menu and calls the selected Triage function."""
    print("\n--- MediGuide AI Triage System ---")
    print("Welcome! Please choose the medical specialty you need help with:")
    print("1: General Physician (Dr. Vital)")
    print("2: Dermatologist (Dr. Luminous)")
    print("3: Psychiatrist (Dr. Insight)")
    print("4: Exit System")

    choice = input("Enter your choice (1, 2, 3, or 4): ")
    
    # Logic: Use if/elif/else to call the correct function
    if choice == '1':
        run_gp_triage()
    elif choice == '2':
        run_derm_triage()
    elif choice == '3':
        run_psych_triage()
    elif choice == '4':
        print("\nThank you for using MediGuide. Stay safe!")
        return
    else:
        print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")
        # If the choice is invalid, call the menu again (a loop)
        main_menu() 

# --------------------------------------------------------------------------1
# FINAL LINE: START THE PROGRAM!
# --------------------------------------------------------------------------
main_menu()


# In[ ]:





# In[ ]:




