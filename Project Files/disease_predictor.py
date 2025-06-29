def predict_disease(symptoms):
    symptoms = symptoms.lower()
    if "fever" in symptoms and "cough" in symptoms:
        return "You might have the Flu. Please consult a doctor for a proper diagnosis."
    elif "headache" in symptoms and "fatigue" in symptoms:
        return "It could be a Migraine or general fatigue. Stay hydrated and rest."
    elif "chest pain" in symptoms:
        return "Chest pain can be serious. Seek immediate medical attention!"
    else:
        return "Unable to predict condition. Please consult a medical professional."
