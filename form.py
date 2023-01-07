import streamlit as st
import pandas as pd

def form_callback(data1, data2):    
    with open('data.csv', 'a+') as f:    #Append & read mode
        f.write(f"{data1},{data2}\n",newline='')

with st.form(key="my_form",clear_on_submit=True):
    
    st.write("Enter Nota")
    
    stock_ticker_input = st.text_input('Stock', key='ticker')
    note_input = st.text_input('Note', key='nota')
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Nota", nota_input, "stock_ticker", stock_ticker_input)
        form_callback(stock_ticker_input,nota_input)

st.info(" #### Show contents of the CSV file :point_down:")
st.dataframe(pd.read_csv("notes.csv",names=["Nombre","Nota"]),height=300)
