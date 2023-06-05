import streamlit as st
import eda
import Prediction

navigation = st.sidebar.selectbox('Pilih Halaman:', ('EDA', 'Predict Location'))

if navigation == 'EDA':
    eda.run()
else:
    Prediction.run()
    