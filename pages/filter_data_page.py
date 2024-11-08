import streamlit as st

def display(raw_data):
    st.header('Filter Data')
    filtered_data = st.text_input("Filter data by IP, Hostnames, Country, etc.", "")
    if filtered_data:
        filtered_df = raw_data.loc[
            raw_data.apply(lambda row: row.astype(str).str.contains(filtered_data, case=False).any(), axis=1)
        ]
        st.write(filtered_df)
    else:
        st.dataframe(raw_data)

data = st.session_state.get('data', None)
if data:
    raw_data = data.get('Raw Data')
    if raw_data is not None:
        display(raw_data)
    else:
        st.error("Raw data sheet 'Raw Data' not found.")
else:
    st.error("No data found.")