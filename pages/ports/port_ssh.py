import streamlit as st
import pandas as pd
import altair as alt

st.title("Product and Port Distribution (Filtered: *ssh*, Not Port 22)")

data = st.session_state.get('data', None)
if data:
    raw_data = data.get('Raw Data', None)
    if raw_data is not None:
        if 'Port' in raw_data.columns and 'Product' in raw_data.columns:
            # Filter for rows where Product contains "ssh" (case-insensitive) and Port is not 22
            ssh_data = raw_data[(raw_data['Product'].str.contains('ssh', case=False, na=False)) & (raw_data['Port'] != 22)]

            if not ssh_data.empty:
                port_product_counts = ssh_data.groupby(['Port', 'Product']).size().reset_index(name='Count')

                st.subheader('Product and Port Counts (Filtered: *ssh*, Not Port 22)')
                st.dataframe(
                    port_product_counts,
                    column_config={
                        "Port": st.column_config.Column(width="medium"),
                        "Product": st.column_config.Column(width="large"),
                        "Count": st.column_config.Column()
                    },
                    height=400,
                    width=702
                )

                chart_port_product = alt.Chart(port_product_counts).mark_bar().encode(
                    x=alt.X('Port:N', sort='-y'),
                    y='Count:Q',
                    color='Product:N',
                    tooltip=['Port', 'Product', 'Count']
                ).properties(
                    title='Product and Port Distribution (Filtered: *ssh*, Not Port 22)',
                    width=702,
                    height=400
                )
                st.altair_chart(chart_port_product)
            else:
                st.info("No data found for Products containing 'ssh' and not on Port 22.")
        else:
            st.error("Columns 'Port' and/or 'Product' not found in the raw data.")
    else:
        st.error("Raw data sheet 'Raw Data' not found.")
else:
    st.error("No data found in session state.")
