import streamlit as st

from src.data_loader import load_data
from src.filters import apply_filters
from src.kpis import show_kpis
from src.charts import (
    sales_over_time,
    sales_by_category,
    sales_by_region
)

st.set_page_config(
    page_title="Dashboard de Análise de Vendas",
    layout="wide"
)

st.title("📊 Dashboard de Análise de Vendas")

# Carregamento dos dados
df = load_data("data/superstore.csv")

# Aplicação dos filtros
df_filtered = apply_filters(df)

# KPIs
show_kpis(df_filtered)

st.divider()

# Gráficos
sales_over_time(df_filtered)
sales_by_category(df_filtered)
sales_by_region(df_filtered)
