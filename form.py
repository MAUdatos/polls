import streamlit as st
import pandas as pd 
   
with st.form(key="my_form",clear_on_submit=True):
    
    st.write("Enter Note")
    
    stock_ticker_input = st.text_input('Stock', key='ticker')
    note_input = st.text_input('Note', key='note')
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Note", note_input, "stock_ticker", stock_ticker_input)
        with open('data.csv', 'a+') as f:    #Append & read mode
            f.write(note_input,stock_ticker_input")

st.info(" #### Show contents of the CSV file :point_down:")
st.dataframe(pd.read_csv("data.csv",names=["Stock","Note"]),height=300)
