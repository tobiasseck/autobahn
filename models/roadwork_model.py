import requests
import streamlit as st

BASE_URL = "https://verkehr.autobahn.de/o/autobahn/"

@st.cache_data(ttl=86400)

def get_roadworks(highway_id):
    """Fetch the roadworks data for a specific highway from the API."""
    try:
        response = requests.get(f"{BASE_URL}{highway_id}/services/roadworks")
        response.raise_for_status()
        return response.json().get("roadworks", [])
    except requests.RequestException as e:
        st.error(f"Fehler beim Abrufen der Baustellen für die Autobahn {highway_id}: {e}")
        return []
    
def process_roadwork_data(roadworks):
    processed_data = []
    for roadwork in roadworks:
        roadwork_data = {
            "title": roadwork.get("title", "Kein Titel"),
            "subtitle": roadwork.get("subtitle", "Kein Untertitel"),
            "description": '\n'.join(roadwork.get('description', [])),
            "coordinate": roadwork.get("coordinate", {}),
            "beginn": "",
            "ende": "",
            "measure_type": "",
            "restrictions": "",
            "max_width": "",
            "length": "",
        }
        processed_data.append(roadwork_data)
    return processed_data