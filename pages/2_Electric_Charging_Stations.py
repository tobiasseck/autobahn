import streamlit as st
import folium
from streamlit_folium import st_folium
from controllers.electric_charging_stations_controller import get_charging_stations_data
from models.utils import select_highway

charging_station_icon_url = "https://upload.wikimedia.org/wikipedia/commons/7/7d/Symbol_electric_vehicle_charging_stations.jpg"

def electric_charging_stations_page():
    selected_highway = select_highway()

    if selected_highway:
        st.title(f"Elektroladestationen auf {selected_highway}")

        charging_stations = get_charging_stations_data(selected_highway)

        m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

        for station in charging_stations:
            lat = float(station["coordinate"].get("lat", 51.1657))
            long = float(station["coordinate"].get("long", 10.4515))

            popup_content = (
                f"<b>{station['title']}</b><br>"
                f"<b>{station['subtitle']}</b><br><br>"
                "<b>Beschreibung:</b><br>" + station['description'].replace('\n', '<br>')
            )

            popup = folium.Popup(popup_content, max_width=300)

            folium.Marker(
                location=(lat, long),
                popup=popup,
                icon=folium.CustomIcon(charging_station_icon_url, icon_size=(32, 32))
            ).add_to(m)

        st_folium(m, width=1400, height=700)

        st.header("Details der Elektroladestationen")
        for station in charging_stations:
            st.markdown(f"### {station['title']}")
            st.markdown(f"**{station['subtitle']}**")
            st.markdown(f"**Beschreibung:**\n{station['description']}")
            st.write("---")

    else:
        st.write("Bitte wählen Sie eine Autobahn aus der Sidebar.")

electric_charging_stations_page()