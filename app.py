import streamlit as st



st.header('aaa')
st.write('aaa')

import pandas as pd
from fbprophet import Prophet

#df = pd.read_csv('/content/example_wp_log_peyton_manning.csv')
df = pd.read_csv('example_wp_log_peyton_manning.csv')

st.write(df.head())











