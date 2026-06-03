import streamlit as st
st.set_page_config(
  page_title="Smart Hospital",
  layout="wide"
)
st.title("🏥 Smart Hospital Patient Navigator")
st.write("Find the Right Department for Your Symptomps")

#symptoms
st.header("Symptoms")

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
chest_pain = st.checkbox("Chest Pain")

#Patient Information
st.header("Patient Information")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=35
)
gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

