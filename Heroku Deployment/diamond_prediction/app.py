import streamlit as st
import numpy as np
from pickle import load

st.title("Diamond Price Prediction")

scaler = load(open('models/standard_scaler.pkl', 'rb'))
rf_model = load(open('models/randomforestregression.pkl', 'rb'))

clarity_encoder = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}
color_encoder = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
cut_encoder = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Ideal': 4, 'Premium': 5}

carat = st.slider('Carat', 0.2, 5.01, 2.5)
table=st.slider('table%',43,95,66)
length=st.slider('Length',0.0,10.7,5.0)
width=st.slider('Width',0.0,58.9,30.0)
depth=st.slider('depth',0.0,31.8,20.0)
lw= length/width


cut = st.selectbox(
    'How would be the cut of Diamond?',
    ('Fair', 'Good', 'Very Good', 'Ideal', 'Premium'))

color = st.selectbox(
    'What should be the color of Diamond?',
    ('J', 'I', 'H', 'G', 'F', 'E', 'D'))

clarity = st.selectbox(
    'How would you like to be contacted?',
    ('I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'))

btn_click = st.button("Predict")

if btn_click == True:
    if carat and lw and table and length and width and depth:

        query_point_num_transformed = scaler.transform(
            [[float(carat), float(table), float(length), float(width), float(depth), float(lw)]])
        query_point_cat = np.array([color_encoder[color], cut_encoder[cut], clarity_encoder[clarity]]) #.reshape(1,-1)

        df = np.concatenate((query_point_cat, query_point_num_transformed.flatten()), axis=None)
        pred = rf_model.predict(df.reshape(1, -1)).item()
        st.success(pred)
        st.balloons()
    else:
        st.error('Enter the values properly')
        st.snow()
