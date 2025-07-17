import streamlit as  st 
import pandas as pd

st.title("Widgets explore....")

# creating a text input box
name=st.text_input("Enter your name: ")
if name:
    st.write(f"Hello! {name} I hope you enjoy streamlit")

# creating a slider, providing the min-max ranges, and the value from which the slider starts

age=st.slider("Enter your age: ", 0,100,20)

if age:
    st.write(f"Your age is: {age}")

# creating a selectbox, which allows us to choose from a variety of options
options=["Python","Java","C++","JavaScript"]
choice=st.selectbox("Choose your favourite language",options)

st.write(f"You chose {choice}")

# printing a dataframe on webapp
df=pd.DataFrame({
    "Name":["Aadrish","Toddy","John","James"],
    "City":["Mumbai","Bangalore","New York","Chicago"]
})

st.write(df)


# reading a csv file
uploaded_file=st.file_uploader("Choose a CSV file to upload",type="csv")


# and then displaying the CSV file as a dataframe on screen
if uploaded_file is not None:
    uploaded_df=pd.read_csv(uploaded_file)
    st.write(uploaded_df)
 