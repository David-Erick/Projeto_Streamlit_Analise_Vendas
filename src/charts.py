import streamlit as st
import plotly.express as px
import pandas as pd

def sales_over_time(df: pd.DataFrame) -> None:
    df_time = (
        df.groupby(df["order_date"].dt.to_period("M"))["sales"]
        .sum()
        .reset_index()
    )

    df_time["order_date"] = df_time["order_date"].astype(str)

    fig = px.line(
        df_time,
        x="order_date",
        y="sales",
        title="📈 Evolução das Vendas ao Longo do Tempo"
    )

    st.plotly_chart(fig, use_container_width=True)


def sales_by_category(df: pd.DataFrame) -> None:
    df_cat = df.groupby("category")["sales"].sum().reset_index()

    fig = px.bar(
        df_cat,
        x="category",
        y="sales",
        title="📊 Vendas por Categoria"
    )

    st.plotly_chart(fig, use_container_width=True)


def sales_by_region(df: pd.DataFrame) -> None:
    df_reg = df.groupby("region")["sales"].sum().reset_index()

    fig = px.pie(
        df_reg,
        names="region",
        values="sales",
        title="🌎 Distribuição de Vendas por Região"
    )

    st.plotly_chart(fig, use_container_width=True)
