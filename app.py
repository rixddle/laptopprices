import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model_filename = 'random_forest_model.pkl'
model = joblib.load(model_filename)

# Title of the app
st.title('Laptop Price Prediction')

# Input features
company = st.selectbox('Company', ['HP', 'Dell', 'Lenovo', 'Asus', 'Apple', 'Acer', 'MSI', 'Toshiba'])
typename = st.selectbox('Type', ['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible'])
ram = st.number_input('RAM (in GB)', min_value=2, max_value=64, step=1)
weight = st.number_input('Weight (in kg)', min_value=0.5, max_value=5.0, step=0.1)
touchscreen = st.selectbox('Touchscreen', ['Yes', 'No'])
ppi = st.number_input('PPI', min_value=100, max_value=400, step=10)
cpu_brand = st.selectbox('CPU Brand', ['Intel', 'AMD', 'Other'])
hdd = st.number_input('HDD (in GB)', min_value=0, max_value=2000, step=50)
ssd = st.number_input('SSD (in GB)', min_value=0, max_value=2000, step=50)
gpu_brand = st.selectbox('GPU Brand', ['Nvidia', 'AMD', 'Intel', 'Other'])
opsys = st.selectbox('Operating System', ['Windows', 'Mac', 'Linux', 'No OS', 'Other'])

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'Company': [company],
    'TypeName': [typename],
    'Ram': [ram],
    'Weight': [weight],
    'Touchscreen': [1 if touchscreen == 'Yes' else 0],
    'PPI': [ppi],
    'Cpu_brand': [cpu_brand],
    'HDD': [hdd],
    'SSD': [ssd],
    'Gpu_brand': [gpu_brand],
    'OpSys_Categorized': [opsys]
})

# Predict the price
if st.button('Predict Price'):
    prediction = model.predict(input_data)
    st.write(f'Predicted Price: ${prediction[0]:.2f}')
