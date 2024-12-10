import streamlit as st
from utils import load_excel
st.set_page_config(page_title="Shodan Data Explorer")


pages = {
    "Ports": [
        st.Page("pages/ports/port_distribution.py", title="Port Distribution"),
        st.Page("pages/ports/port_53.py", title="Port 53"),
    ],
    "Products": [
        st.Page("pages/products/product_info.py", title="Product Info"),
    ],
    "Test": [
        st.Page("pages/test/filter_data_page.py", title="Filter Data"),
        st.Page("pages/test/raw_data_page.py", title="Raw Data"),
        st.Page("pages/test/summary_data_page.py", title="Summary Data"),
    ],
}

pg = st.navigation(pages)

default_file_path = 'data/shodan_data_9k.xlsx'
data = load_excel(default_file_path)

if data and isinstance(data, dict):
    st.session_state['data'] = data


else:
    st.error("Error reading the file or the file format is incorrect.")


pg.run()
