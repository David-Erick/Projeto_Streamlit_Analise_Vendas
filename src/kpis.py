import streamlit as st
import pandas as pd

def show_kpis(df: pd.DataFrame) -> None:
    total_sales = df["sales"].sum()
    total_orders = df.shape[0]
    avg_ticket = total_sales / total_orders if total_orders > 0 else 0

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Vendas Totais", f"R$ {total_sales:,.2f}")
    col2.metric("🛒 Total de Pedidos", total_orders)
    col3.metric("🎟️ Ticket Médio", f"R$ {avg_ticket:,.2f}")
