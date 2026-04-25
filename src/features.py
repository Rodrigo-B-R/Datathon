import pandas as pd
import numpy as np


def transacciones_por_usuario(transacciones: pd.DataFrame) -> pd.DataFrame:
    """Aggregate transaction-level features to user level."""
    return (
        transacciones.groupby("user_id")
        .agg(
            num_transacciones=("transaccion_id", "count"),
            monto_total=("monto", "sum"),
            monto_promedio=("monto", "mean"),
            num_categorias=("categoria_mcc", "nunique"),
            pct_internacional=("es_internacional", "mean"),
            pct_atipico=("patron_uso_atipico", "mean"),
            cashback_total=("cashback_generado", "sum"),
        )
        .reset_index()
    )


def categoria_pivot(transacciones: pd.DataFrame) -> pd.DataFrame:
    """One-hot spending share per MCC category per user."""
    pivot = (
        transacciones.groupby(["user_id", "categoria_mcc"])["monto"]
        .sum()
        .unstack(fill_value=0)
    )
    # Normalize to spending share
    pivot = pivot.div(pivot.sum(axis=1), axis=0)
    pivot.columns = [f"cat_{c}" for c in pivot.columns]
    return pivot.reset_index()


def perfil_usuario(clientes: pd.DataFrame, transacciones: pd.DataFrame) -> pd.DataFrame:
    """Join demographic features with transaction aggregates."""
    agg = transacciones_por_usuario(transacciones)
    cats = categoria_pivot(transacciones)
    return clientes.merge(agg, on="user_id", how="left").merge(cats, on="user_id", how="left")
