import streamlit as st
import pandas as pd
import plotly.express as px
from models.roadwork_model import get_roadworks
from models.road_closure_model import get_road_closures
from models.warnings_model import get_warnings
from models.electric_charging_stations_model import get_electric_charging_stations

st.set_page_config(layout="wide")

def home_page():
    st.title("Highway Statistics in Germany")

    highways = [f"A{i}" for i in range(1, 10)]
    data = {"Highway": highways, "Roadworks": [], "Closures": [], "Warnings": [], "Charging Stations": []}

    for highway in highways:
        data["Roadworks"].append(len(get_roadworks(highway)))
        data["Closures"].append(len(get_road_closures(highway)))
        data["Warnings"].append(len(get_warnings(highway)))
        data["Charging Stations"].append(len(get_electric_charging_stations(highway)))

    df = pd.DataFrame(data)
    df.set_index("Highway", inplace=True)

    st.subheader("Comparative Statistics of Major Highways")
    st.dataframe(df)

    fig_roadworks = px.bar(df, x=df.index, y="Roadworks", title="Number of Roadworks per Highway",
                           labels={"Highway": "Highway", "Roadworks": "Number of Roadworks"},
                           template="plotly_dark")

    fig_closures = px.bar(df, x=df.index, y="Closures", title="Number of Closures per Highway",
                          labels={"Highway": "Highway", "Closures": "Number of Closures"},
                          template="plotly_dark")

    fig_warnings = px.bar(df, x=df.index, y="Warnings", title="Number of Warnings per Highway",
                          labels={"Highway": "Highway", "Warnings": "Number of Warnings"},
                          template="plotly_dark")

    fig_charging = px.bar(df, x=df.index, y="Charging Stations", title="Number of Charging Stations per Highway",
                          labels={"Highway": "Highway", "Charging Stations": "Number of Charging Stations"},
                          template="plotly_dark")

    for fig in [fig_roadworks, fig_closures, fig_warnings, fig_charging]:
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )
        st.plotly_chart(fig, use_container_width=True)

home_page()
