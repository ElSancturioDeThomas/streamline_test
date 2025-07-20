import streamlit as st

st.title("Unit Converter: Meters to Feet")

meters = st.number_input("Enter meters:")
feet = meters * 3.28084
st.write(f"{meters} meters is {feet:.2f} feet.")
