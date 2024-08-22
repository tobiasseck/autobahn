from models.roadwork_model import get_roadworks, process_roadwork_data

def get_roadworks_data(highway):
    raw_data = get_roadworks(highway)
    processed_data = process_roadwork_data(raw_data)
    return processed_data