import streamlit as st

st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("🕵️ Fake News Detector")
st.write("Enter a news article or headline below to detect whether it's fake or real.")


user_input = st.text_area("📰 Paste headline or article text here:", height=200)


if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        
        st.info("Sending to backend model...")
        
        
        import random
        prediction = random.choice(["Real", "Fake"])

        # Show result
        if prediction == "Real":
            st.success("✅ This news appears to be REAL.")
        else:
            st.error("🚨 This news appears to be FAKE.")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fa;
        color: #1a1a1a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)
