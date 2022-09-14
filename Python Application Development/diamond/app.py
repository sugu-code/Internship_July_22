import streamlit as st
import pandas as pd
from pickle import load

df=pd.read_csv('Data/diamonds.csv')

# Loading pretrained models from pickle file
or_enc=load(open('models/ordinal_encoder.pkl','rb'))
scaler = load(open('models/standard_scaler.pkl', 'rb'))
dt_regressor=load(open('models/DecisionTree_model.pkl','rb'))




#Please fill all the Diamond properties

with st.form('my_form'):
    carat = st.select_slider('Select a Input of Carat', options=df.carat.unique())
    cut = st.selectbox(label='Select Cut of Diamond', options=df.cut.unique())
    color = st.selectbox(label='Select Color of Diamond', options=df.color.unique())
    clarity= st.selectbox(label='Select Clarity level of Diamond', options=df.clarity.unique())
    depth=st.select_slider('Select a depth of Diamond', options=df.depth.unique())
    table=st.select_slider('Select a table of Diamond', options=df.table.unique())


    
    buttn = st.form_submit_button(label='Predict')


if buttn:
    if carat and cut and color and clarity and depth and table:
        query_num = pd.DataFrame({'carat':[carat], 'depth':[depth],'table':[table]})
        query_cat = pd.DataFrame({'cut':[cut], 'color':[color], 'clarity':[clarity]})
        query_cat = or_enc.transform(query_cat)
        query_num = scaler.transform(query_num)
        query_point = pd.concat([pd.DataFrame(query_num), pd.DataFrame(query_cat)], axis=1)
        price = dt_regressor.predict(query_point)
        
        st.success(f"The price of Selected Diamond is $ {round(price[0],2)}")
    else:
        st.error('Enter all the values')    
        st.snow()
