import streamlit as st
import folium
from streamlit_folium import st_folium
from controllers.webcam_controller import get_webcams, process_webcam_data
from models.utils import select_highway

webcam_icon_url = "https://upload.wikimedia.org/wikipedia/commons/a/aa/Camera-icon.svg"

def webcams_page():
    selected_highway = select_highway()

    if selected_highway:
        st.title(f"Verkehrskameras auf {selected_highway}")

        webcams = get_webcams(selected_highway)
        processed_webcams = process_webcam_data(webcams)

        m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

        for webcam in processed_webcams:
            lat = float(webcam["coordinate"].get("lat", 51.1657))
            long = float(webcam["coordinate"].get("long", 10.4515))

            popup_content = (
                f"<b>{webcam['title']}</b><br>"
                f"<b>{webcam['subtitle']}</b><br><br>"
                f'<img src="{webcam["imageurl"]}" width="100%" height="auto"><br>'
                f'<a href="{webcam["linkurl"]}" target="_blank">Live Stream ansehen</a>'
            )

            popup = folium.Popup(popup_content, max_width=600)

            folium.Marker(
                location=(lat, long),
                popup=popup,
                tooltip=webcam['title'],
                icon=folium.CustomIcon(webcam_icon_url, icon_size=(32, 32))
            ).add_to(m)

        st_folium(m, width=1400, height=700)

webcams_page()
