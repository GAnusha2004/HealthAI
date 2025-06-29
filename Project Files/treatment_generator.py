def generate_treatment(condition):
    condition = condition.lower()
    if "diabetes" in condition:
        return (
            "🩸 Treatment Plan for Diabetes:\n"
            "- Medication: Metformin, Insulin (if needed)\n"
            "- Diet: Low sugar, high fiber\n"
            "- Exercise: 30 mins/day\n"
            "- Monitor: Blood glucose daily\n"
            "- Regular doctor follow-up"
        )
    elif "hypertension" in condition:
        return (
            "💓 Treatment Plan for Hypertension:\n"
            "- Medication: Amlodipine, ACE inhibitors\n"
            "- Diet: Low salt, avoid oily food\n"
            "- Exercise: Walking, yoga\n"
            "- Monitor: Blood pressure regularly\n"
            "- Reduce stress and caffeine"
        )
    else:
        return (
            "⚠️ No specific treatment found for this condition.\n"
            "Please consult a certified medical professional."
        )
