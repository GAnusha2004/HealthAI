def ask_ai(query):
    query = query.lower()
    if "headache" in query:
        return "For headaches, stay hydrated and rest. If it persists, consult a doctor."
    elif "cold" in query or "cough" in query:
        return "You may have a common cold. Drink warm fluids and rest. If symptoms worsen, seek medical advice."
    elif "emergency" in query or "pain" in query:
        return "Please visit a nearby hospital or call emergency services immediately."
    else:
        return "I'm here to help! For detailed answers, please consult a certified healthcare provider."
