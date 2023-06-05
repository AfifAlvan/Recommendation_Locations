import streamlit as st
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 
from PIL import Image
import numpy as np
import joblib
import json


st.set_page_config(
    page_title ='Recommendation Location',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    st.title ('LOCATION-BASED RECOMMENDATION')
    st.subheader('Exploratory Data Analys')

    st.write('''Hai This is **Recommendation Location** from Lumbung AI''')

    image = Image.open('haha.jpeg')
    st.image(image, caption = 'Finding Location For Your Business')

    st.markdown('---')
    
if __name__ == '__main__':
    run()