import requests
import streamlit as st

BASE_URL = "https://verkehr.autobahn.de/o/autobahn/"

@st.cache_data(ttl=3600)
def get_warnings(highway_id):
    try:
        response = requests.get(f"{BASE_URL}{highway_id}/services/warning")
        response.raise_for_status()
        return response.json().get("warning", [])
    except requests.RequestException as e:
        st.error(f"Fehler beim Abrufen der Warnmeldungen für die Autobahn {highway_id}: {e}")
        return []

def process_warning_data(warnings):
    processed_data = []
    for warning in warnings:
        warning_data = {
            "title": warning.get("title", "Kein Titel"),
            "subtitle": warning.get("subtitle", "Kein Untertitel"),
            "description": '\n'.join(warning.get('description', [])),
            "coordinate": warning.get("coordinate", {}),
        }
        processed_data.append(warning_data)
    return processed_data
