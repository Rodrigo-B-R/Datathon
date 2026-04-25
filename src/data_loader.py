import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "Data"
LOCAL_DATA_DIR = Path(__file__).parent.parent / "data"


def load_clientes() -> pd.DataFrame:
    return pd.read_csv(LOCAL_DATA_DIR / "hey_clientes.csv")


def load_productos() -> pd.DataFrame:
    return pd.read_csv(LOCAL_DATA_DIR / "hey_productos.csv")


def load_transacciones() -> pd.DataFrame:
    return pd.read_csv(LOCAL_DATA_DIR / "hey_transacciones.csv", parse_dates=["fecha_hora"])


def load_conversaciones() -> pd.DataFrame:
    df = pd.read_parquet(DATA_DIR / "Conversaciones" / "dataset_50k_anonymized.parquet")
    df["date"] = pd.to_datetime(df["date"])
    return df


def load_all() -> dict[str, pd.DataFrame]:
    return {
        "clientes": load_clientes(),
        "productos": load_productos(),
        "transacciones": load_transacciones(),
        "conversaciones": load_conversaciones(),
    }
