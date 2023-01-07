import pandas as pd
import streamlit as st

FILE_TYPES = ["csv"]

file = st.file_uploader("Upload .csv file", type=FILE_TYPES)
if file is not None:
    data = pd.read_csv(file)
    st.dataframe(data.head(10))
    
    dataframe = {
        "DateTime": ["ss"],
        "Name": ["s"],
        "Email": ["ese"],
        "Target User": ["csc"],
        "Alternate Target": ["dsd"],
        "Questions": ["ese"]
    }

    # Write the dataframe to a CSV file
    df = pd.DataFrame(dataframe)
    df.to_csv("data.csv")

    # Write dataframe to streamlit 
    st.dataframe(df) 

    # Allow the user to download the new CSV file
    st.download_file(file, "data.csv")
