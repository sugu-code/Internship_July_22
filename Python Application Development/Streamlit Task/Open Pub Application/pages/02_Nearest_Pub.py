#import requirements
import numpy as np
import pandas as pd
import streamlit as st
import app 

#importing data
res=app.df[['lat','lon']]
res['lat']=res['lat'].astype('float64')
res['lon']=res['lon'].astype('float64')
#displaing nearest pubs
st.title("PUBS Near you")
st.subheader("Enter your location details to find nearest 5 PUBS")
#Entering latitude information
lat = st.number_input('Enter your Latitude (Ex: 51.968239):')
st.write('Your Latitude is ', lat)
#enter your longitude information
lon = st.number_input('Enter your Longitude (Ex: 1.030394):')
st.write('Your Longitude is ', lon)
test=np.array([lat,lon])
test_df=pd.DataFrame(test.reshape(1,2),columns=['lat','lon'])

#Finding nearest 5 Pubs
distances=np.sqrt(np.sum((res-test)**2,axis=1))
app.df=app.df.assign(distance=distances)
k=5
min_indices=np.argpartition(distances,k-1)[:k]
res=res[res.index.isin(min_indices)]

#displaying the map for particular local authority
button_click= st.button('Find Now')
if button_click==True: 
    st.map(res)
    st.text("The location corresponding to below minimum distances : ")
    st.dataframe(app.df.iloc[min_indices])