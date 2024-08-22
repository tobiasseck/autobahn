import requests
import streamlit as st

BASE_URL = "https://verkehr.autobahn.de/o/autobahn/"

def get_highways():
    """Fetch the list of highways from the API."""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json().get("roads", [])
    except requests.RequestException as e:
        st.error(f"Error fetching highways: {e}")
        return []
