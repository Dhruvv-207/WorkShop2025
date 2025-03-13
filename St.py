import streamlit as st 
import pandas as pd
import numpy as np 

st.title("My First Cloud App")
st.write("A Simple DataFrames")

df = pd.DataFrame(np.random.randn(10,2),columns=['cols1','cols2'])
st.dataframe(df)