import streamlit as st
import folium
from streamlit_folium import st_folium
from controllers.warnings_controller import get_warnings_data
from models.utils import select_highway

warning_icon_url = "https://upload.wikimedia.org/wikipedia/commons/0/02/Zeichen_101_-_Gefahrstelle%2C_StVO_1970.svg"

def traffic_warnings_page():
    selected_highway = select_highway()

    if selected_highway:
        st.title(f"Verkehrswarnungen auf {selected_highway}")

        warnings = get_warnings_data(selected_highway)

        m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

        for warning in warnings:
            lat = float(warning["coordinate"].get("lat", 51.1657))
            long = float(warning["coordinate"].get("long", 10.4515))

            popup_content = (
                f"<b>{warning['title']}</b><br>"
                f"<b>{warning['subtitle']}</b><br><br>"
                "<b>Beschreibung:</b><br>" + warning['description'].replace('\n', '<br>')
            )

            popup = folium.Popup(popup_content, max_width=300)

            folium.Marker(
                location=(lat, long),
                popup=popup,
                icon=folium.CustomIcon(warning_icon_url, icon_size=(32, 32))
            ).add_to(m)

        st_folium(m, width=1400, height=700)

        st.header("Details der Verkehrswarnungen")
        for warning in warnings:
            st.markdown(f"### {warning['title']}")
            st.markdown(f"#####{warning['subtitle']}")
            st.markdown(f"**Beschreibung:**\n{warning['description']}")
            st.write("---")

    else:
        st.write("Bitte wählen Sie eine Autobahn aus der Sidebar.")

traffic_warnings_page()
