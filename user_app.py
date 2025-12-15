import streamlit as st
import pandas as pd
from gemini_utils import analyze_feedback

st.title("📝 Feedback Form")

feedback = st.text_area("Enter your feedback")

if st.button("Submit"):
    sentiment = analyze_feedback(feedback)

    st.success(f"Sentiment: {sentiment}")

    df = pd.DataFrame([[feedback, sentiment]], columns=["feedback", "sentiment"])
    df.to_csv("feedback.csv", mode="a", header=False, index=False)
