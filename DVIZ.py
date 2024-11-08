import streamlit as st
from utils import load_excel

# Set page config for the app
st.set_page_config(page_title="Shodan Data Explorer")

# Load the default file
default_file_path = 'shodan_data.xlsx'
data = load_excel(default_file_path)

if data and isinstance(data, dict):
    st.session_state['data'] = data


else:
    st.error("Error reading the file or the file format is incorrect.")