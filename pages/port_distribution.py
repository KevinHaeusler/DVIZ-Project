import streamlit as st
import pandas as pd
import altair as alt

def display(raw_data):
    st.header('Ports Distribution')

    if 'Port' in raw_data.columns:
        port_counts = raw_data['Port'].value_counts().reset_index()
        port_counts.columns = ['Port', 'Count']

        chart = alt.Chart(port_counts).mark_bar().encode(
            x=alt.X('Port:N', sort='-y'),
            y='Count:Q',
            tooltip=['Port', 'Count']
        ).properties(
            title='Ports Distribution',
            width=800,
            height=400
        )

        st.altair_chart(chart)
    else:
        st.error("Column 'Port' not found in raw data.")

data = st.session_state.get('data', None)
if data:
    raw_data = data.get('Raw Data')
    if raw_data is not None:
        display(raw_data)
    else:
        st.error("Raw data sheet 'Raw Data' not found.")
else:
    st.error("No data found.")