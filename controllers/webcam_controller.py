from models.webcam_model import get_webcams

def process_webcam_data(webcams):
    processed_data = []
    for webcam in webcams:
        webcam_data = {
            "title": webcam.get("title", "Kein Titel"),
            "subtitle": webcam.get("subtitle", "Keine Blickrichtung"),
            "coordinate": webcam.get("coordinate", {}),
            "imageurl": webcam.get("imageurl", ""),
            "linkurl": webcam.get("linkurl", ""),
        }
        processed_data.append(webcam_data)
    return processed_data
