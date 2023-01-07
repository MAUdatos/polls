import csv
import streamlit as st
import pandas as pd 

f = open('data.csv','w')
writer = csv.writer(f)

with st.form(key="my_form",clear_on_submit=True):
    
    st.write("Enter Note")
    
    stock_ticker_input = st.text_input('Stock', key='ticker')
    note_input = st.text_input('Note', key='note')
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        writer.writerow(note_input)
