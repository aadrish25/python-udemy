import streamlit as st 
import pandas as pd
import numpy as np


# creating the title of application
st.title("Hello Streamlittt!")


# write simple texts
st.write("This is a simple text")


# create a simple dataframe and print it
df=pd.DataFrame({
    "Column A":[1,2,3,4],
    "Column B":[10,20,30,40]
})

# display the dataframe on the webpage
st.write("Here is the dataframe: ")
st.write(df)


# also display a line chart
st.line_chart(df)