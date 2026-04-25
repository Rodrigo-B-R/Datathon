# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

This is a data science competition project for **Hey Banco Datathon 2026** — a Mexican digital bank. All data is 100% synthetic. The primary language of the data is Spanish.

## Data Overview

Two independent datasets live under `Data/`:

### Conversaciones (`Data/Conversaciones/`)
Customer support conversations between users and an AI assistant ("Havi"). Loaded via Parquet (the CSV is gitignored).

```python
import pandas as pd
df = pd.read_parquet("Data/Conversaciones/dataset_50k_anonymized.parquet")
# Group by conv_id to reconstruct full multi-turn conversations
conv = df[df["conv_id"] == "some-uuid"].sort_values("date")
```

Key columns: `input`, `output`, `date`, `conv_id`, `user_id`, `channel_source` (1=text, 2=voice).

### Transacciones (`Data/Transacciones/`)
Three relational CSV files (gitignored — must be obtained separately):

| File | Description |
|------|-------------|
| `hey_clientes.csv` | One row per user — demographics, credit score, behavioral signals |
| `hey_productos.csv` | Products per user — accounts, cards, loans, investments, insurance |
| `hey_transacciones.csv` | Transaction history — one row per movement |

**Join keys:**
- `hey_clientes.user_id` → `hey_productos.user_id` → `hey_transacciones.user_id`
- `hey_productos.producto_id` → `hey_transacciones.producto_id`

Notable fields in `hey_transacciones.csv`: `tipo_operacion` (13 operation types), `canal` (9 channels), `categoria_mcc` (14 MCC categories), `cashback_generado` (1% for Hey Pro users on completed purchases), `patron_uso_atipico` (unusual activity flag).

Notable fields in `hey_clientes.csv`: `score_buro` (295–850), `es_hey_pro`, `nomina_domiciliada`, `satisfaccion_1_10` (NPS 1–10), `patron_uso_atipico`.

Full data dictionaries are in `Data/Transacciones/DICCIONARIO_DATOS.md` and `Data/Conversaciones/README.md`.

## Data Loading Pattern

```python
import pandas as pd

# Transactions dataset
clientes = pd.read_csv("Data/Transacciones/hey_clientes.csv")
productos = pd.read_csv("Data/Transacciones/hey_productos.csv")
transacciones = pd.read_csv("Data/Transacciones/hey_transacciones.csv")

# Conversations dataset
convs = pd.read_parquet("Data/Conversaciones/dataset_50k_anonymized.parquet")
```

## .gitignore Notes

All `*.csv` files are gitignored. Only `dataset_50k_anonymized.parquet` is tracked. When adding analysis scripts, track notebooks and Python files but not derived CSVs.
