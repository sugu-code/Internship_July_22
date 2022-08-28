#import requirements
import streamlit as st
import pandas as pd
import numpy as np

#reading dataset
df=pd.read_csv('data/open_pubs.csv')
#assigning column names to the dataset
df.columns=['fsa_id','name','address','postcode','easting','northing','lat','lon','local_authority']
#replacing '\N' with null value
df=df.replace('\\N',np.NaN)
#removing null value rows
df=df.dropna()

#finding unique local_authority 
data_selection =df.local_authority.unique()
#displaying details
pub="Total no of PUBS: "+str(df.shape[0])
auth="Total no of PUB's Local Authority: "+str(data_selection.shape[0])
lat_range= "Latitude Range: "+str(df['lat'].min())+" to "+str(df['lat'].max())
lon_range= "Longitude Range: "+str(df['lon'].min())+" to "+str(df['lon'].max())

st.title("OPEN PUB APPLICATION ")
st.subheader("Time for some drinks")
st.dataframe(df.head())

st.subheader(pub)
st.subheader(auth)
st.subheader(lat_range)
st.subheader(lon_range)
st.sidebar.success("Select your required page")

