import streamlit as st
import folium
from streamlit_folium import st_folium
from controllers.road_closure_controller import get_closures_data
from models.utils import select_highway

closure_icon_url = "https://upload.wikimedia.org/wikipedia/commons/4/46/Zeichen_250_-_Verbot_f%C3%BCr_Fahrzeuge_aller_Art%2C_StVO_1970.svg"

def road_closures_page():
    selected_highway = select_highway()

    if selected_highway:
        st.title(f"Sperrungen auf {selected_highway}")

        closures = get_closures_data(selected_highway)

        m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

        for closure in closures:
            lat = float(closure["coordinate"].get("lat", 51.1657))
            long = float(closure["coordinate"].get("long", 10.4515))

            popup_content = (
                f"<b>{closure['title']}</b><br>"
                f"<b>{closure['subtitle']}</b><br><br>"
                "<b>Beschreibung:</b><br>" + closure['description'].replace('\n', '<br>')
            )

            popup = folium.Popup(popup_content, max_width=300)

            folium.Marker(
                location=(lat, long),
                popup=popup,
                icon=folium.CustomIcon(closure_icon_url, icon_size=(32, 32))
            ).add_to(m)

        st_folium(m, width=1400, height=700)

        st.header("Details der Sperrungen")
        for closure in closures:
            st.markdown(f"### {closure['title']}")
            st.markdown(f"#####{closure['subtitle']}")
            st.markdown(f"**Beschreibung:**\n{closure['description']}")
            st.write("---")

    else:
        st.write("Bitte wählen Sie eine Autobahn aus der Sidebar.")

road_closures_page()
