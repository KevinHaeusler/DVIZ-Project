import streamlit as st
import pandas as pd

# Function to load Excel file
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

# Streamlit app
st.title("Shodan Data Explorer")
st.sidebar.header("Upload Excel file if you want to use a different one")

# Define default file path
default_file_path = 'data/shodan_data_9k.xlsx'

# File uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx"])

# Use uploaded file if available, otherwise use default file
file_to_load = uploaded_file if uploaded_file else default_file_path

# Load the selected file
data = load_excel(file_to_load)

if isinstance(data, dict):
    raw_data = data.get('Raw Data')
    summary_data = data.get('Summary')

    if raw_data is not None:
        st.header('Raw Data')
        st.write(raw_data.head())
        st.write(f"Total Rows: {len(raw_data.index)}")

        # Adding a filtering option for better interactivity
        filtered_data = st.text_input("Filter data by IP, Hostnames, Country, etc.", "")
        if filtered_data:
            filtered_df = raw_data.loc[
                raw_data.apply(lambda row: row.astype(str).str.contains(filtered_data, case=False).any(), axis=1)
            ]
            st.write(filtered_df)
        else:
            st.dataframe(raw_data)
    else:
        st.error("Raw data sheet 'raw data' not found.")

    if summary_data is not None:
        st.header('Summary Data')
        st.write(summary_data.head())

        # Extract total devices and display
        st.subheader('Summary Statistics')
        try:
            total_devices = summary_data.loc[summary_data.index[0], 'Total']
            st.write(f"Total Devices Scanned: {total_devices}")
        except KeyError as e:
            st.error(f"Error in Summary sheet structure: {e}")

        st.subheader('Ports Distribution')
        try:
            ports_distribution = summary_data[['Ports Distribution']]
            st.bar_chart(ports_distribution)
        except KeyError as e:
            st.error(f"Error in Summary sheet structure: {e}")
    else:
        st.error("Summary sheet 'summary' not found.")
else:
    st.error("Error reading the file or the file format is incorrect.")