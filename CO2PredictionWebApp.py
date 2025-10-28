# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 12:41:23 2025

@author: Muizzah
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
import streamlit as st


with open("C02_model.sav", "rb") as f:
    loaded_model = cloudpickle.load(f)
    
def co2(features):

    feature_names = ['Make', 'Model', 'Vehicle Class', 'Engine Size(L)', 'Cylinders',
           'Transmission', 'Fuel Type', 'Fuel Consumption City (L/100 km)',
           'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)',
           'Fuel Consumption Comb (mpg)']
    features_dataframe = pd.DataFrame([features], columns=feature_names)
    prediction = loaded_model.predict(features_dataframe)
    return prediction
     


def main():
     
    st.title("CO2 Emission prediction Web App")
    make = st.text_input("Enter the vehicle make (e.g., Toyota, Ford): ")
    model = st.text_input("Enter the vehicle model (e.g., Camry, F-150): ")
    vehicle_class = st.text_input("Enter the vehicle class (e.g., SUV, Sedan): ")
    engine_size = st.number_input("Enter the engine size in liters (e.g., 2.5): ")
    cylinders = st.number_input("Enter the number of cylinders (e.g., 4, 6): ")
    transmission = st.text_input("Enter the transmission type (e.g., Automatic, Manual): ")
    fuel_type = st.text_input("Enter the fuel type (e.g., Gasoline, Diesel): ")
    fuel_consumption_city = st.number_input("Enter fuel consumption in city (L/100 km): ")
    fuel_consumption_hwy = st.number_input("Enter fuel consumption on highway (L/100 km): ")
    fuel_consumption_comb = st.number_input("Enter combined fuel consumption (L/100 km): ")
    fuel_consumption_mpg = st.number_input("Enter combined fuel consumption (mpg): ")
    
    
    C02 = ''
    if st.button('C02 Emission result'):                                  
        C02 = co2([make, model, vehicle_class, engine_size, cylinders,
        transmission, fuel_type, fuel_consumption_city, fuel_consumption_hwy,
        fuel_consumption_comb, fuel_consumption_mpg])

    st.success(C02)
    

if __name__ == '__main__':

    main()



