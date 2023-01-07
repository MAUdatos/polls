import streamlit as st
import pandas as pd

with st.form(key="my_form",clear_on_submit=True):
    
    st.write("Enter Note")   
    stock_ticker_input = st.text_input('Nombre', key='ticker')
    note_input = st.text_input('Nota', key='note')
    submitted = st.form_submit_button("Subir")
    if submitted:
        fields = ['Nombre','Nota']
        with open('data.csv', 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        
     
