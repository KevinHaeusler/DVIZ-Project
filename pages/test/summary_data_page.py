import streamlit as st

def display(summary_data):
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

data = st.session_state.get('data', None)
if data:
    summary_data = data.get('Summary')
    if summary_data is not None:
        display(summary_data)
    else:
        st.error("Summary sheet 'SUMMARY' not found.")
else:
    st.error("No data found.")