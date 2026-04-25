import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_loader import load_clientes, load_transacciones
from src.features import perfil_usuario

st.set_page_config(page_title="Hey Banco — Motor de Inteligencia", layout="wide")
st.title("Motor de Inteligencia & Atención Personalizada")
st.caption("Hey Banco Datathon 2026")

st.info("Demo en construcción. Carga los datos en `data/` para comenzar.")
