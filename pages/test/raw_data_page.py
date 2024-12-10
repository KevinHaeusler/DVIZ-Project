import streamlit as st

def display(raw_data):
    st.header('Raw Data')
    st.write(raw_data.head())
    st.write(f"Total Rows: {len(raw_data.index)}")
    st.dataframe(raw_data)

data = st.session_state.get('data', None)
if data:
    raw_data = data.get('Raw Data')
    if raw_data is not None:
        display(raw_data)
    else:
        st.error("Raw data sheet 'RAW DATA' not found.")
else:
    st.error("No data found.")