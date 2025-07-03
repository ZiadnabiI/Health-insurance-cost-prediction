# app.py (Corrected Version)
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Insurance Charge Predictor",
    layout="centered"
)

@st.cache_resource
def load_model_and_scaler():
    """Load the saved model and scaler."""
    model = joblib.load('insurance_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

model, scaler = load_model_and_scaler()

# ---  Page Title and UI Elements ---
st.title("Insurance Charge Predictor 🩺")
st.write("Enter your details below to get an estimated insurance charge.")

# User Input Section
col1, col2 = st.columns(2)
with col1:
    age = st.slider("Age", 18, 100, 30)
    sex = st.selectbox("Sex", ("male", "female"))
    smoker = st.selectbox("Smoker", ("no", "yes"))
    
with col2:
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0, format="%.2f")
    children = st.number_input("Number of Children" ,min_value=0 , max_value=20 , value=0  )
    region = st.selectbox("Region", ("southwest", "southeast", "northwest", "northeast"))

# Prediction Logic
if st.button("Predict Charge", use_container_width=True):
    input_data = {
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'children': children,
        'smoker': smoker,
        'region': region
    }
    input_df = pd.DataFrame([input_data])
    
    # Preprocessing
    input_df['sex'] = input_df['sex'].map({'female': 0, 'male': 1})
    input_df['smoker'] = input_df['smoker'].map({'no': 0, 'yes': 1})
    region_dummies = pd.get_dummies(input_df['region'], drop_first=True, dtype=int)
    input_df = pd.concat([input_df.drop('region', axis=1), region_dummies], axis=1)
    
    training_columns = ['age', 'sex', 'bmi', 'children', 'smoker', 
                        'region_northwest', 'region_southeast', 'region_southwest']
                        
    input_df = input_df.reindex(columns=training_columns, fill_value=0)
    
    scaled_features = scaler.transform(input_df)

    prediction = model.predict(scaled_features)

    st.success(f"Predicted Insurance Charge: ${prediction[0]:,.2f}")