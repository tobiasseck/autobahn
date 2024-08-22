# Autobahn

Autobahn is a small application that provides up-to-date data related to the German Autobahn using its public API. The app is built with Python and is designed to fetch and display relevant information about traffic, road conditions, and other essential data concerning the German Autobahn network.

## Features

- Fetches real-time data from the German Autobahn API.
- Displays information in an easy-to-read format.
- Built using Python.
- Designed following the MVC (Model-View-Controller) architecture.

## Architecture

The application follows the MVC (Model-View-Controller) structure:

- **Model**: Handles the data retrieval and processing. It interacts with the German Autobahn API and manages the data structures used in the app.
- **View**: Responsible for the user interface, built with Streamlit, to present the data to the user in a user-friendly format.
- **Controller**: Acts as the intermediary between the Model and the View, handling user input, updating the View with new data from the Model, and ensuring that the data flow and application logic are properly maintained.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tobiasseck/autobahn.git
   ```
2. Navigate to the project directory:
   ```bash
   cd autobahn
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with:
```bash
streamlit run Home.py
```

This will start a Streamlit server, where you can view the application in your browser.

## License

This project is licensed under the MIT License.

---

You can view the project live [here](https://autobahn.streamlit.app/).
