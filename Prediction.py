import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np
import joblib
import json
import pickle

# load

with open('dataai.json', 'r') as f1:
    data_inf = pd.read_json(f1)

data_inf = st.dataframe(data_inf)

def my_func(row, cluster, ses, provinsi):
    if row['cluster'] == cluster and row['ses'] == ses and row['provinsi'] == provinsi:
        return True
    else:
        return False

def run():
    st.title ('LOCATION-BASED RECOMMENDATION')
    st.subheader('Input what you want here!!!')
    # Membuat Form
    with st.form(key='Parameter'):
        nama = st.text_input('Name', value='')
        cluster = st.number_input('Cluster', min_value=0, max_value=1, value=0, step=1)
        ses = st.selectbox('SES(Social Economic Status)', ('A', 'B', 'C1', 'C2', 'D', 'E'))
        provinsi = st.text_input('provinsi', value='')

        st.markdown('----')

        submitted = st.form_submit_button('Rekomendasi')

    if submitted:
        filtered_data = data_inf.apply(my_func, args=(cluster, ses, provinsi), axis=1)
        st.write(f'We recommend this location for you! Good Luck !! ',data_inf[filtered_data][:1])
        st.write(f'THANK YOU :)')  
   
if __name__ == '__eda__':
    run()