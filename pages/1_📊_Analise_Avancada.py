import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data

st.set_page_config(
    page_title="Análise Avançada",
    layout="wide"
)

st.title("📊 Análise Avançada de Vendas")
st.caption("Exploração dinâmica com foco em insights estratégicos")

# ===============================
# 🔹 Carregamento dos dados
# ===============================
df = load_data("data/superstore.csv")

# ===============================
# 🎛️ CONTROLES AVANÇADOS
# ===============================
with st.container():
    st.subheader("🎛️ Controles")

    col1, col2, col3 = st.columns(3)

    with col1:
        region = st.selectbox(
            "Região",
            options=["Todas"] + sorted(df["region"].dropna().unique().tolist())
        )

    with col2:
        category = st.selectbox(
            "Categoria",
            options=["Todas"] + sorted(df["category"].dropna().unique().tolist())
        )

    with col3:
        aggregation = st.radio(
            "Agregação temporal",
            ["Mensal", "Trimestral"],
            horizontal=True
        )

# Aplicação dos filtros
df_filtered = df.copy()

if region != "Todas":
    df_filtered = df_filtered[df_filtered["region"] == region]

if category != "Todas":
    df_filtered = df_filtered[df_filtered["category"] == category]

# ===============================
# 📦 CARDS MODERNOS (KPIs)
# ===============================
with st.container():
    st.subheader("📦 Visão Geral")

    total_sales = df_filtered["sales"].sum()
    avg_sales = df_filtered["sales"].mean()
    max_sale = df_filtered["sales"].max()

    c1, c2, c3 = st.columns(3)

    c1.metric("💰 Vendas Totais", f"R$ {total_sales:,.2f}")
    c2.metric("📊 Venda Média", f"R$ {avg_sales:,.2f}")
    c3.metric("🔥 Maior Venda", f"R$ {max_sale:,.2f}")

# ===============================
# 📈 TABS DE ANÁLISE
# ===============================
tab1, tab2 = st.tabs(["📈 Tendência Temporal", "📦 Distribuição"])

with tab1:
    if aggregation == "Mensal":
        df_time = (
            df_filtered
            .groupby(df_filtered["order_date"].dt.to_period("M"))["sales"]
            .sum()
            .reset_index()
        )
        df_time["periodo"] = df_time["order_date"].astype(str)
    else:
        df_time = (
            df_filtered
            .groupby(df_filtered["order_date"].dt.to_period("Q"))["sales"]
            .sum()
            .reset_index()
        )
        df_time["periodo"] = df_time["order_date"].astype(str)

    fig = px.area(
        df_time,
        x="periodo",
        y="sales",
        title="Evolução das Vendas",
    )

    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.box(
        df_filtered,
        x="category",
        y="sales",
        title="Distribuição de Vendas por Categoria"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===============================
# 🔎 INSIGHTS RÁPIDOS
# ===============================
with st.expander("🔎 Insights Automáticos"):
    st.markdown(
        f"""
        - 💡 **Registros analisados:** {len(df_filtered)}
        - 🏆 **Categoria com maior venda média:**  
          `{df_filtered.groupby("category")["sales"].mean().idxmax()}`
        - 🌍 **Região dominante:**  
          `{df_filtered.groupby("region")["sales"].sum().idxmax()}`
        """
    )
