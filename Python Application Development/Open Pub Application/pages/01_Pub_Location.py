#import requirements
import numpy as np
import pandas as pd
import streamlit as st
import app 

#displaing the information
st.title("PUB Location")
st.header("Select a Local Authority")

#choosing a local authority
option = st.selectbox(
    'Select a Local Authority',
     app.data_selection)

'You selected: ', option

#displaying the map for particular local authority
button_click= st.button('Find Now')
if button_click==True: 
    res= app.df[app.df['local_authority']==option]
    res['lat']=res['lat'].astype('float64')
    res['lon']=res['lon'].astype('float64')
    res=res[['lat','lon']]
    st.map(res)
    