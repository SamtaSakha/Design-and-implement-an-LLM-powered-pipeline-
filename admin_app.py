
import os
import pandas as pd
import streamlit as st
from pandas.errors import EmptyDataError

st.title("📊 Admin Dashboard")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "feedback.csv")

try:
    df = pd.read_csv(CSV_PATH)
except EmptyDataError:
    df = pd.DataFrame(columns=["feedback", "sentiment"])

st.dataframe(df)
