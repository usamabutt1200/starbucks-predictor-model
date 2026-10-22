import streamlit as st
import joblib
import pandas as pd

# Starbucks Model load karein
model = joblib.load('starbucks_model.pkl')

st.title("☕ Starbucks Offer Predictor")
st.write("Customer ki details enter karein taake check kiya ja sakay ke woh offer complete karega ya nahi:")

# User inputs (Starbucks data ke mutabiq)
age = st.slider("Customer Age", 18, 100, 30)
income = st.number_input("Annual Income ($)", 10000, 150000, 50000)
gender = st.selectbox("Gender", ["Female", "Male"])
offer_type = st.selectbox("Offer Received", ["Discount Offer", "BOGO (Buy One Get One)"])

# Inputs ko binary format mein badalna
gender_m = 1 if gender == "Male" else 0
discount_offer = 1 if offer_type == "Discount Offer" else 0

# DataFrame banana sahi column order ke sath
input_data = pd.DataFrame([{
    'Age': age, 
    'Income': income, 
    'Gender_M': gender_m, 
    'Discount_Offer': discount_offer
}])

# Prediction Button
if st.button("Predict Customer Response"):
    prediction = model.predict(input_data)
    if prediction == 1:
        st.success("🎉 Customer yeh offer **COMPLETE** karega!")
    else:
        st.error("❌ Customer is offer ko **IGNORE** kar dega.")
