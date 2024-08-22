import requests
import streamlit as st

BASE_URL = "https://verkehr.autobahn.de/o/autobahn/"

@st.cache_data(ttl=86400)
def get_road_closures(highway_id):
    try:
        response = requests.get(f"{BASE_URL}{highway_id}/services/closure")
        response.raise_for_status()
        return response.json().get("closure", [])
    except requests.RequestException as e:
        st.error(f"Fehler beim Abrufen der Sperrungen für die Autobahn {highway_id}: {e}")
        return []

def process_closure_data(closures):
    processed_data = []
    for closure in closures:
        closure_data = {
            "title": closure.get("title", "Kein Titel"),
            "subtitle": closure.get("subtitle", "Kein Untertitel"),
            "description": '\n'.join(closure.get('description', [])),
            "coordinate": closure.get("coordinate", {}),
        }
        processed_data.append(closure_data)
    return processed_data
