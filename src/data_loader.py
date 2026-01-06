import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # 🔥 Padronizar nomes das colunas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Converter data corretamente
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        dayfirst=True,
        errors="coerce"
    )

    return df
