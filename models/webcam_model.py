import requests
import streamlit as st

BASE_URL = "https://verkehr.autobahn.de/o/autobahn/"

@st.cache_data(ttl=86400)
def get_webcams(highway_id):
    try:
        response = requests.get(f"{BASE_URL}{highway_id}/services/webcam")
        response.raise_for_status()
        return response.json().get("webcam", [])
    except requests.RequestException as e:
        st.error(f"Fehler beim Abrufen der Webcams für die Autobahn {highway_id}: {e}")
        return []
