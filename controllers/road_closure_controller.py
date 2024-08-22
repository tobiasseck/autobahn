from models.road_closure_model import get_road_closures, process_closure_data

def get_closures_data(highway):
    raw_data = get_road_closures(highway)
    processed_data = process_closure_data(raw_data)
    return processed_data