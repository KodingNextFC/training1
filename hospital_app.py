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

