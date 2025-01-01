import streamlit as st
import altair as alt

def display(raw_data):
    st.header('Ports Distribution')

    if 'Port' in raw_data.columns:
        # Count occurrences of each port
        port_counts = raw_data['Port'].value_counts().reset_index()
        port_counts.columns = ['Port', 'Count']

        # DataFrame for top 10 ports
        top_10_ports = port_counts.head(10)
        top_10_ports = top_10_ports.reset_index(drop=True)
        top_10_ports.index = top_10_ports.index + 1

        st.subheader('All Ports Distribution')
        st.dataframe(
            port_counts,
            column_config={
                "index": st.column_config.Column(),
                "Port": st.column_config.Column(width="large"),
                "Count": st.column_config.Column()
            },
            height=400,
            width=702
        )

        chart_all = alt.Chart(port_counts).mark_bar().encode(
            x=alt.X('Port:N', sort='-y'),
            y='Count:Q',
            tooltip=['Port', 'Count']
        ).properties(
            title='All Ports Distribution',
            width=702,
            height=400
        )
        st.altair_chart(chart_all)

        st.subheader('Top 10 Ports')
        st.dataframe(
            top_10_ports,
            column_config={
                "index": st.column_config.Column(),
                "Port": st.column_config.Column(width="large"),
                "Count": st.column_config.Column()
            },
            height=400,
            width=702
        )

        chart_top_10 = alt.Chart(top_10_ports.reset_index()).mark_bar().encode(
            x=alt.X('Port:N', sort='-y'),
            y='Count:Q',
            tooltip=['Port', 'Count']
        ).properties(
            title='Top 10 Ports Distribution',
            width=702,
            height=400
        )
        st.altair_chart(chart_top_10)

        st.markdown("Here we can see the overall ports distribution and a closer look at the top 10 used ports.")
        st.markdown("Port 443 and Port 80 are HTTPS and HTTP respectively. This is expected because most applications display a webpage to access them.")

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


