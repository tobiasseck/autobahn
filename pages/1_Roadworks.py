import streamlit as st
import folium
from streamlit_folium import st_folium
from controllers.roadwork_controller import get_roadworks_data
from models.utils import select_highway

construction_sign_icon_url = "https://upload.wikimedia.org/wikipedia/commons/7/78/Zeichen_123_-_Baustelle%2C_StVO_1992.svg"

def roadworks_page():
    selected_highway = select_highway()

    if selected_highway:
        st.title(f"Straßenbauarbeiten auf {selected_highway}")

        roadworks = get_roadworks_data(selected_highway)

        m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

        for roadwork in roadworks:
            lat = float(roadwork["coordinate"].get("lat", 51.1657))
            long = float(roadwork["coordinate"].get("long", 10.4515))

            popup_content = (
                f"<b>{roadwork['title']}</b><br>"
                f"<b>{roadwork['subtitle']}</b><br><br>"
                "<b>Beschreibung:</b><br>" + roadwork['description'].replace('\n', '<br>')
            )

            popup = folium.Popup(popup_content, max_width=300)

            folium.Marker(
                location=(lat, long),
                popup=popup,
                icon=folium.CustomIcon(construction_sign_icon_url, icon_size=(32, 32))
            ).add_to(m)

        st_folium(m, width=1400, height=700)

        st.header("Details der Straßenbauarbeiten")
        for roadwork in roadworks:
            st.markdown(f"### {roadwork['title']}")
            st.markdown(f"#####{roadwork['subtitle']}")
            st.markdown(f"**Beschreibung:**\n{roadwork['description']}")
            st.write("---")

    else:
        st.write("Bitte wählen Sie eine Autobahn aus der Sidebar.")

roadworks_page()