import streamlit as st
import pandas as pd
import altair as alt

def display(raw_data):
    st.header('Product Information')

    # Ensure the 'Product' column exists; if not, create it with "N/A"
    if 'Product' not in raw_data.columns:
        raw_data['Product'] = 'N/A'

    # Replace NaNs in the 'Product' column with "N/A"
    raw_data['Product'].fillna('N/A', inplace=True)

    # DataFrame for all products
    product_counts = raw_data['Product'].value_counts().reset_index()
    product_counts.columns = ['Product', 'Count']

    # DataFrame for top 10 products excluding "N/A"
    top_10_products = product_counts[product_counts['Product'] != 'N/A'].head(10)

    # Column configuration
    st.subheader('All Products Distribution')
    st.dataframe(
        product_counts,
        column_config={
            "index": st.column_config.Column(),
            "Product": st.column_config.Column(width="large"),
            "Count": st.column_config.Column()
        },
        height=400,
        width=702
    )

    # Display a bar chart for all products distribution
    chart_all = alt.Chart(product_counts).mark_bar().encode(
        x=alt.X('Product:N', sort='-y'),
        y='Count:Q',
        tooltip=['Product', 'Count']
    ).properties(
        title='All Products Distribution',
        width=702,
        height=400
    )

    st.altair_chart(chart_all)

    st.markdown("Only half of the collected data returns a product information.")

    st.subheader('Top 10 Products (excluding N/A)')
    st.dataframe(
        top_10_products,
        column_config={
            "index": st.column_config.Column(),
            "Product": st.column_config.Column(width="large"),
            "Count": st.column_config.Column()
        },
        height=400,
        width=702
    )

    # Display a bar chart for top 10 products distribution excluding "N/A"
    chart_top_10 = alt.Chart(top_10_products).mark_bar().encode(
        x=alt.X('Product:N', sort='-y'),
        y='Count:Q',
        tooltip=['Product', 'Count']
    ).properties(
        title='Top 10 Products Distribution (excluding N/A)',
        width=702,
        height=400
    )

    st.altair_chart(chart_top_10)
    st.markdown('''Looking at the 10 most used products we can see that the top 3 are Postfix SMTPD (for sending e-mail) nginx (for hosting websites) and OpenSSH (for access to the system). 
    
    
                This is an expected distribution of products. Interesting is that there are 62 Chromecasts accessible ''')

data = st.session_state.get('data', None)
if data:
    raw_data = data.get('Raw Data')
    if raw_data is not None:
        display(raw_data)
    else:
        st.error("Raw data sheet 'Raw Data' not found.")
else:
    st.error("No data found.")