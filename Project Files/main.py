import streamlit as st
from disease_predictor import predict_disease
from treatment_generator import generate_treatment
from chat_interface import ask_ai
from analytics_dashboard import show_dashboard

st.title("🩺 HealthAI: Intelligent Healthcare Assistant")

menu = st.sidebar.radio("Choose a Service", ["Disease Prediction", "Treatment Plan", "Health Analytics", "Patient Chat"])

if menu == "Disease Prediction":
    st.header("🤒 Disease Prediction")
    symptoms = st.text_area("Enter your symptoms (comma separated):")
    if st.button("Predict"):
        result = predict_disease(symptoms)
        st.success(result)

elif menu == "Treatment Plan":
    st.header("💊 Treatment Plan Generator")
    condition = st.text_input("Enter diagnosed condition:")
    if st.button("Generate Plan"):
        plan = generate_treatment(condition)
        st.info(plan)

elif menu == "Health Analytics":
    st.header("📈 Health Analytics Dashboard")
    show_dashboard()

elif menu == "Patient Chat":
    st.header("💬 Ask HealthAI")
    query = st.text_input("Ask a medical question:")
    if st.button("Ask"):
        response = ask_ai(query)
        st.write(response)
