import requests
import streamlit as st

BASE_URL = "https://verkehr.autobahn.de/o/autobahn/"

@st.cache_data(ttl=86400)
def get_electric_charging_stations(highway_id):
    try:
        response = requests.get(f"{BASE_URL}{highway_id}/services/electric_charging_station")
        response.raise_for_status()
        return response.json().get("electric_charging_station", [])
    except requests.RequestException as e:
        st.error(f"Fehler beim Abrufen der Ladestationen für die Autobahn {highway_id}: {e}")
        return []

def process_charging_station_data(stations):
    processed_data = []
    for station in stations:
        station_data = {
            "title": station.get("title", "Kein Titel"),
            "subtitle": station.get("subtitle", "Kein Untertitel"),
            "description": '\n'.join(station.get('description', [])),
            "coordinate": station.get("coordinate", {}),
        }
        processed_data.append(station_data)
    return processed_data
