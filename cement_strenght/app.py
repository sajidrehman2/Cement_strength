import joblib
import streamlit as st
import numpy as np

# Load the trained model
ridge_model = joblib.load("ridge_model.pkl")

# Page title
st.title("Concrete Strength Prediction App")
st.write("This app predicts concrete compressive strength based on component data.")

# User inputs for features
st.header("Input the features:")
cement = st.number_input("Cement (component 1) (kg in a m^3 mixture)", min_value=0.0)
blast_furnace_slag = st.number_input("Blast Furnace Slag (component 2) (kg in a m^3 mixture)", min_value=0.0)
fly_ash = st.number_input("Fly Ash (component 3) (kg in a m^3 mixture)", min_value=0.0)
water = st.number_input("Water (component 4) (kg in a m^3 mixture)", min_value=0.0)
superplasticizer = st.number_input("Superplasticizer (component 5) (kg in a m^3 mixture)", min_value=0.0)
coarse_aggregate = st.number_input("Coarse Aggregate (component 6) (kg in a m^3 mixture)", min_value=0.0)
fine_aggregate = st.number_input("Fine Aggregate (component 7) (kg in a m^3 mixture)", min_value=0.0)
age = st.number_input("Age (days)", min_value=1)

# Convert inputs to numpy array
input_features = np.array([[cement, blast_furnace_slag, fly_ash, water,
                            superplasticizer, coarse_aggregate, fine_aggregate, age]])

# Make prediction
if st.button("Predict Concrete Strength"):
    prediction = ridge_model.predict(input_features)
    st.success(f"Predicted Concrete Strength: {prediction[0]:.2f} MPa")
