import streamlit as st
import altair as alt

st.title("ISP Distribution for Port 53")

data = st.session_state.get('data', None)
if data:
    raw_data = data.get('Raw Data', None)
    if raw_data is not None:
        if 'Port' in raw_data.columns and 'ISP' in raw_data.columns:
            port_53_data = raw_data[raw_data['Port'] == 53]

            if not port_53_data.empty:
                isp_counts_53 = port_53_data['ISP'].value_counts().reset_index()
                isp_counts_53.columns = ['ISP', 'Count']

                isp_counts_53 = isp_counts_53.reset_index(drop=True)
                isp_counts_53.index = isp_counts_53.index + 1

                st.subheader('ISP Counts for Port 53')
                st.dataframe(
                    isp_counts_53,
                    column_config={
                        "index": st.column_config.Column(),
                        "ISP": st.column_config.Column(width="large"),
                        "Count": st.column_config.Column()
                    },
                    height=400,
                    width=702
                )

                chart_isp_53 = alt.Chart(isp_counts_53.reset_index()).mark_bar().encode(
                    x=alt.X('ISP:N', sort='-y'),
                    y='Count:Q',
                    tooltip=['ISP', 'Count']
                ).properties(
                    title='ISP Distribution for Port 53',
                    width=702,
                    height=400
                )
                st.altair_chart(chart_isp_53)
            else:
                st.info("No data found for Port 53.")
        else:
            st.error("Columns 'Port' and/or 'ISP' not found in the raw data.")
    else:
        st.error("Raw data sheet 'Raw Data' not found.")
else:
    st.error("No data found in session state.")
