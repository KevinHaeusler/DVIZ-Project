import streamlit as st
import pandas as pd

st.title("Interactive Data Filtering")

if "data" in st.session_state:
    raw_data = st.session_state["data"]["Raw Data"]

    st.subheader("Original Dataset")
    st.dataframe(raw_data)

    st.subheader("Filters")

    selected_columns = st.multiselect(
        "Select columns to display:",
        raw_data.columns.tolist(),
        default=raw_data.columns.tolist(),
    )

    col1, col2, col3 = st.columns(3)
    filters = {}

    for idx, column in enumerate(raw_data.columns):
        col = [col1, col2, col3][idx % 3]

        if raw_data[column].dtype == "object":
            unique_values = raw_data[column].dropna().unique().tolist()
            filters[column] = col.multiselect(
                f"Filter by {column}:",
                options=unique_values,
                default=[],
                key=f"filter_{column}",
            )
        elif pd.api.types.is_numeric_dtype(raw_data[column]):
            filters[column] = col.slider(
                f"Filter by {column} (range):",
                min_value=float(raw_data[column].min()),
                max_value=float(raw_data[column].max()),
                value=(float(raw_data[column].min()), float(raw_data[column].max())),
                key=f"filter_{column}",
            )
        elif pd.api.types.is_datetime64_any_dtype(raw_data[column]):
            filters[column] = col.date_input(
                f"Filter by {column} (range):",
                value=(
                    raw_data[column].min().date(),
                    raw_data[column].max().date(),
                ),
                key=f"filter_{column}",
            )

    filtered_data = raw_data.copy()
    for column, filter_value in filters.items():
        if isinstance(filter_value, list) and filter_value:
            filtered_data = filtered_data[filtered_data[column].isin(filter_value)]
        elif isinstance(filter_value, tuple) and len(filter_value) == 2:  #
            if pd.api.types.is_numeric_dtype(raw_data[column]):
                filtered_data = filtered_data[
                    (filtered_data[column] >= filter_value[0]) & (filtered_data[column] <= filter_value[1])
                ]
            elif pd.api.types.is_datetime64_any_dtype(raw_data[column]):
                filtered_data = filtered_data[
                    (filtered_data[column] >= pd.Timestamp(filter_value[0])) & (filtered_data[column] <= pd.Timestamp(filter_value[1]))
                ]

    st.subheader("Filtered Dataset")
    st.dataframe(filtered_data[selected_columns])

    st.download_button(
        label="Download Filtered Data as CSV",
        data=filtered_data[selected_columns].to_csv(index=False).encode("utf-8"),
        file_name="filtered_data.csv",
        mime="text/csv",
    )
else:
    st.error("No data found in session state. Please load the dataset first.")
