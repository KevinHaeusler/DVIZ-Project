import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def categorize_products(raw_data):
    category_rules = {
        "Web": {
            "ports": [80, 443],
            "keywords": ["nginx", "apache", "iis", "lighthttpd"],
        },
        "Mail": {
            "ports": [25],
            "keywords": ["smtp", "exchange", "smtpd", "imap"],
        },
        "Services": {
            "ports": [53],
            "keywords": ["dns", "snmp", "ssh", "remote desktop protocol", "rdp"],
        },
        "Databases": {
            "ports": [],
            "keywords": ["mariadb", "sql"],
        },
        "IoT": {
            "ports": [],
            "keywords": ["nas", "synology", "webcam", "chromecast", "router",
                         "sonos", "spotify", "tv", "qnap", "synology"],
        },
    }

    def categorize(row):
        if pd.isnull(row['Product']) or str(row['Product']).strip() == "":
            return "N/A"

        product = str(row['Product']).lower()
        port = row['Port']

        for category, rules in category_rules.items():
            if port in rules['ports'] or any(keyword in product for keyword in rules['keywords']):
                return category

        return "Other"

    raw_data['Category'] = raw_data.apply(categorize, axis=1)
    return raw_data

st.title("Product Categorization and Pie Chart")

data = st.session_state.get('data', None)

if data:
    raw_data = data.get('Raw Data', None)
    if raw_data is not None:
        if 'Port' in raw_data.columns and 'Product' in raw_data.columns:
            categorized_data = categorize_products(raw_data)

            category_counts = categorized_data['Category'].value_counts()

            st.subheader("Categorized Product Distribution (Pie Chart)")

            fig, ax = plt.subplots(
                figsize=(8, 6)
            )

            wedges, texts, autotexts = ax.pie(
                category_counts,
                labels=category_counts.index,
                autopct=lambda pct: f"{pct:.1f}%"
                if pct > 3
                else "",
                startangle=90,
                textprops=dict(color="w"),
            )

            legend_labels = [
                f"{label} ({count})"
                for label, count in zip(category_counts.index, category_counts.values)
            ]

            ax.legend(
                wedges,
                legend_labels,
                title="Categories",
                loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1),
            )

            ax.axis("equal")
            st.pyplot(fig)


            st.subheader("Categorized Data Table")
            st.dataframe(categorized_data)

        else:
            st.error("Columns 'Port' and/or 'Product' not found in the raw data.")
    else:
        st.error("Raw data sheet 'Raw Data' not found in session state.")
else:
    st.error("No data found in session state.")
