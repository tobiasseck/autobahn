from models.warnings_model import get_warnings, process_warning_data

def get_warnings_data(highway):
    raw_data = get_warnings(highway)
    processed_data = process_warning_data(raw_data)
    return processed_data