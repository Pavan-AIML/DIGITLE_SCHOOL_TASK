import streamlit as st
import pandas as pd
from pydantic import BaseModel
# from fastapi import FastAPI, Body, Query
# from pydantic import BaseModel
# import uvicorn
from typing import Dict
import pickle
import json

st.title("Predicted Number of the Accidents.")

with st.sidebar:
    st.header("Input data requirement")
    st.caption("The data must be enter in the form of Year and month individual values.")
    with st.expander("Data format"):
        st.markdown("year -: XXXX ")
        st.markdown("month -: X or XX")
    st.divider()
    st.caption("<p style = 'text-align:center'> Developed by Pavan Kumar</p>", unsafe_allow_html = True)

# Taking the input data as year and month. 

year = int(st.number_input("Enter the value of year:", step =1, format = "%d"))
month = int(st.number_input("Enter the value of month:", step = 1, format = "%d"))


# Adding the button.

if st.button("Click here to find the predicted values of the accidents"):

    pickle_in = open("regression_model.pkl", "rb") # rb is mode to open pikle file
    regression_model = pickle.load(pickle_in)
    predicted_values = regression_model.predict([[year, month]])
    predicted_values= int(predicted_values)
    st.markdown(f"<h1 style='color:white;'>{predicted_values}</h1>", unsafe_allow_html=True)
    

    


