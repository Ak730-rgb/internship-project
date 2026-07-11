import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_rent_pipeline.pkl")

st.set_page_config(page_title="House Rent Prediction", page_icon="🏠")

st.title("🏠 House Rent Prediction System")

city = st.selectbox(
    "City",
    ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad"]
)

bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)

size = st.number_input("Size (Square Feet)", min_value=100, value=1000)

floor = st.text_input("Floor", "1 out of 5")

area_type = st.selectbox(
    "Area Type",
    [
        "Super Area",
        "Carpet Area",
        "Built Area"
    ]
)

area_locality = st.text_input("Area Locality")

furnishing = st.selectbox(
    "Furnishing Status",
    [
        "Unfurnished",
        "Semi-Furnished",
        "Furnished"
    ]
)

tenant = st.selectbox(
    "Tenant Preferred",
    [
        "Bachelors",
        "Family",
        "Bachelors/Family"
    ]
)

bathroom = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

contact = st.selectbox(
    "Point of Contact",
    [
        "Contact Owner",
        "Contact Agent",
        "Contact Builder"
    ]
)

if st.button("Predict Rent"):

    input_data = pd.DataFrame({
        "BHK": [bhk],
        "Size": [size],
        "Floor": [floor],
        "Area Type": [area_type],
        "Area Locality": [area_locality],
        "City": [city],
        "Furnishing Status": [furnishing],
        "Tenant Preferred": [tenant],
        "Bathroom": [bathroom],
        "Point of Contact": [contact]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Monthly Rent = ₹ {prediction[0]:,.0f}")