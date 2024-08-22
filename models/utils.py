import streamlit as st
from models.highway_model import get_highways

def select_highway():
    highways = get_highways()

    if "selected_highway" not in st.session_state:
        st.session_state["selected_highway"] = highways[4]

    selected_highway = st.sidebar.selectbox(
        "Select a highway:",
        highways,
        index=highways.index(st.session_state["selected_highway"])
    )

    if selected_highway != st.session_state["selected_highway"]:
        st.session_state["selected_highway"] = selected_highway

    return st.session_state["selected_highway"]
