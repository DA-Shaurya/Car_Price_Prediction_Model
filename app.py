import streamlit as st
import pickle
import pandas as pd 

model = pickle.load(open('model.pkl', 'rb'))
cols = pickle.load(open('columns.pkl', 'rb'))

st.title('Car Price Prediction')

insurance_validity = st.selectbox('Insurance validity:', 
    ['Comprehensive','Third Party','Third Party insurance','Zero Dep','Not Available'])

fuel_type = st.selectbox('Fuel Type:', 
    ['Petrol','Diesel','CNG'])

kms_driven = st.number_input('KMs Driven:', min_value=0)

ownsership = st.selectbox('Ownership:', 
    ['First Owner','Second Owner','Third Owner','Fourth Owner','Fifth Owner'])

transmission = st.selectbox('Transmission Type:', 
    ['Manual','Automatic'])

if st.button('Predict'):
    
    test = pd.DataFrame([{
        'insurance_validity': insurance_validity,
        'fuel_type': fuel_type,
        'kms_driven': kms_driven,
        'ownsership': ownsership,
        'transmission': transmission
    }])

    test = pd.get_dummies(test)
    test = test.reindex(columns=cols, fill_value=0)

    yp = int(model.predict(test)[0])
    
    st.success(f'Predicted Car Price is {yp} Rs.')