import streamlit as st
import pandas as pd

def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("🔎 Filtros")

    region = st.sidebar.multiselect(
        "Região",
        options=sorted(df["region"].dropna().unique()),
        default=sorted(df["region"].dropna().unique())
    )

    category = st.sidebar.multiselect(
        "Categoria",
        options=sorted(df["category"].dropna().unique()),
        default=sorted(df["category"].dropna().unique())
    )

    min_date = df["order_date"].min()
    max_date = df["order_date"].max()

    date_range = st.sidebar.date_input(
        "Período",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    filtered_df = df[
        (df["region"].isin(region)) &
        (df["category"].isin(category)) &
        (df["order_date"].dt.date >= date_range[0]) &
        (df["order_date"].dt.date <= date_range[1])
    ]

    return filtered_df
