import streamlit as st
import random

st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("Fake News Detector")

enter_input = st.text_area("Enter headline or article of news", height=200)

if st.button("Detect"):
    if enter_input.strip() == "":
        st.warning("Please enter")
    else:
        with st.spinner("Analyzing news..."):
            predicted_ans = random.choice(["Real", "Fake"])
            st.session_state.predicted_ans = predicted_ans  # store in session

if "predicted_ans" in st.session_state:
    if st.session_state.predicted_ans == "Real":
        st.success("This News is Real")
    else:
        st.error("This news is Fake")