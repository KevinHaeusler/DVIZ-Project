import streamlit as st
import pandas as pd

@st.cache_data
def load_excel(file):
    try:
        # Read all sheets into a dictionary of DataFrames
        xls = pd.ExcelFile(file)
        data = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}
        return data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return str(e)