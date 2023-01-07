import csv
import streamlit as st

st.title("Form_Demo")
st.subheader("details etc.")

with st.form("form1", clear_on_submit=True):
    name = st.text_input("enter full name")
    email = st.text_input("enter email")
    satisfaction = st.slider("How much do you like our Web App?",
    min_value = 0, max_value=10)
    st.write(satisfaction)

    submit = st.form_submit_button("Submit this form")

data = ["This", "is", "a", "Test"]
with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    
dataframe = {
        "DateTime": ["ss"],
        "Name": ["s"],
        "Email": ["ese"],
        "Target User": ["csc"],
        "Alternate Target": ["dsd"],
        "Questions": ["ese"]
    }

dataframe.to_csv('data.csv')
