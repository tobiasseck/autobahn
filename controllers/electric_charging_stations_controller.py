from models.electric_charging_stations_model import get_electric_charging_stations, process_charging_station_data

def get_charging_stations_data(highway):
    raw_data = get_electric_charging_stations(highway)
    processed_data = process_charging_station_data(raw_data)
    return processed_data