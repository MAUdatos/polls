import streamlit as st
import pandas as pd
#import numpy as np
#import plotly.express as px
#import matplotlib.pyplot as plt
#import re

#__________________________________________________________________________________________________________________________________________________________________
# Dashboard structure
#__________________________________________________________________________________________________________________________________________________________________
st.set_page_config(page_title="MAU ", page_icon="🍃", layout="wide")

# Hide index when showing a table. CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# data
df_poll = pd.read_csv('Sistematización y Mapeo MAU. Reacciones y visiones sobre futuros avances. .csv',sep=',').dropna(how = 'all')   # Base de datos respuestas poll 01.07.2023
df_poll2 = df_poll.iloc[:,2:] 

st.caption('<div style="text-align: left">Sistematización y Mapeo. Prototipo Web App  1.0</div>', unsafe_allow_html=True)          
#st.image("logo_mau.png", width=125)

st.header("Resultados de feedback sobre la herramienta. 2023.")
st.markdown("  ")
st.table(df_poll2)
