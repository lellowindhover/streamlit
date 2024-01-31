import streamlit as st

def calculate_performance_coefficient(temperature, pressure):
    # Placeholder formula, replace it with your actual performance coefficient calculation
    performance_coefficient = temperature * pressure / 100
    return performance_coefficient

def main():
    st.title("HVAC Performance Coefficient Calculator")

    # Input for temperature
    temperature = st.slider("Temperature (in Celsius)", min_value=0, max_value=100, value=25)
