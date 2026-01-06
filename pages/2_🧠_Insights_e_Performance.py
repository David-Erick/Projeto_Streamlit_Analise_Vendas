import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data

st.set_page_config(
    page_title="Insights & Performance",
    layout="wide"
)

# ===============================
# 🎨 CSS CUSTOMIZADO
# ===============================
st.markdown("""
<style>
.kpi-card {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 20px;
    border-radius: 16px;
    color: white;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}
.kpi-title {
    font-size: 14px;
    opacity: 0.85;
}
.kpi-value {
    font-size: 32px;
    font-weight: bold;
    margin-top: 5px;
}
.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Insights & Performance")
st.caption("Análise estratégica do mix de produtos, logística e concentração de vendas")

# ===============================
# 📥 Dados
# ===============================
df = load_data("data/superstore.csv")

# ===============================
# 📦 KPIs CUSTOMIZADOS
# ===============================
total_sales = df["sales"].sum()
num_products = df["product_name"].nunique()
num_cities = df["city"].nunique()

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Vendas Totais</div>
        <div class="kpi-value">R$ {total_sales:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Produtos Únicos</div>
        <div class="kpi-value">{num_products}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Cidades Atendidas</div>
        <div class="kpi-value">{num_cities}</div>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# 🏆 TOP PRODUTOS
# ===============================
st.markdown('<div class="section-title">🏆 Produtos com Maior Receita</div>', unsafe_allow_html=True)

top_products = (
    df.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="sales",
    y="product_name",
    orientation="h",
    title="Top 10 Produtos por Vendas",
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# 📦 MIX DE CATEGORIAS
# ===============================
st.markdown('<div class="section-title">📦 Mix de Categorias e Subcategorias</div>', unsafe_allow_html=True)

mix = (
    df.groupby(["category", "sub_category"])["sales"]
    .sum()
    .reset_index()
)

fig = px.treemap(
    mix,
    path=["category", "sub_category"],
    values="sales",
    title="Composição do Faturamento"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# 🚚 IMPACTO DO ENVIO
# ===============================
st.markdown('<div class="section-title">🚚 Impacto do Modo de Envio</div>', unsafe_allow_html=True)

ship = (
    df.groupby("ship_mode")["sales"]
    .mean()
    .reset_index()
)

fig = px.bar(
    ship,
    x="ship_mode",
    y="sales",
    title="Venda Média por Modo de Envio"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# 🏙️ CONCENTRAÇÃO GEOGRÁFICA
# ===============================
st.markdown('<div class="section-title">🏙️ Concentração Geográfica</div>', unsafe_allow_html=True)

cities = (
    df.groupby("city")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    cities,
    x="city",
    y="sales",
    title="Top 10 Cidades por Vendas"
)

st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data

st.set_page_config(
    page_title="Insights e Performance",
    layout="wide"
)

# ===============================
# 🎨 CSS CUSTOMIZADO
# ===============================
st.markdown("""
<style>
.kpi-card {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 20px;
    border-radius: 16px;
    color: white;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}
.kpi-title {
    font-size: 14px;
    opacity: 0.85;
}
.kpi-value {
    font-size: 32px;
    font-weight: bold;
    margin-top: 5px;
}
.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 🧠 TÍTULO
# ===============================
st.title("🧠 Insights e Performance")
st.caption("Análise estratégica do mix de produtos, logística e concentração de vendas")

# ===============================
# 📥 DADOS
# ===============================
df = load_data("data/superstore.csv")

# ===============================
# 📊 KPIs PRINCIPAIS
# ===============================
total_sales = df["sales"].sum()
num_products = df["product_name"].nunique()
num_cities = df["city"].nunique()

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Faturamento Total</div>
        <div class="kpi-value">R$ {total_sales:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Produtos Distintos</div>
        <div class="kpi-value">{num_products}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Cidades Atendidas</div>
        <div class="kpi-value">{num_cities}</div>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# 🏆 PRODUTOS COM MAIOR FATURAMENTO
# ===============================
st.markdown(
    '<div class="section-title">🏆 Produtos com Maior Faturamento</div>',
    unsafe_allow_html=True
)

top_products = (
    df.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="sales",
    y="product_name",
    orientation="h",
    title="Top 10 Produtos por Faturamento",
    labels={
        "sales": "Faturamento (R$)",
        "product_name": "Produto"
    }
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# 📦 MIX DE CATEGORIAS
# ===============================
st.markdown(
    '<div class="section-title">📦 Mix de Categorias e Subcategorias</div>',
    unsafe_allow_html=True
)

mix = (
    df.groupby(["category", "sub_category"])["sales"]
    .sum()
    .reset_index()
)

fig = px.treemap(
    mix,
    path=["category", "sub_category"],
    values="sales",
    title="Composição do Faturamento por Categoria",
    labels={
        "sales": "Faturamento (R$)",
        "category": "Categoria",
        "sub_category": "Subcategoria"
    }
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# 🚚 IMPACTO DO MODO DE ENVIO
# ===============================
st.markdown(
    '<div class="section-title">🚚 Impacto do Modo de Envio</div>',
    unsafe_allow_html=True
)

ship = (
    df.groupby("ship_mode")["sales"]
    .mean()
    .reset_index()
)

fig = px.bar(
    ship,
    x="ship_mode",
    y="sales",
    title="Venda Média por Modo de Envio",
    labels={
        "ship_mode": "Modo de Envio",
        "sales": "Venda Média (R$)"
    }
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# 🏙️ CONCENTRAÇÃO GEOGRÁFICA
# ===============================
st.markdown(
    '<div class="section-title">🏙️ Concentração Geográfica das Vendas</div>',
    unsafe_allow_html=True
)

cities = (
    df.groupby("city")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    cities,
    x="city",
    y="sales",
    title="Top 10 Cidades por Faturamento",
    labels={
        "city": "Cidade",
        "sales": "Faturamento (R$)"
    }
)

st.plotly_chart(fig, use_container_width=True)
