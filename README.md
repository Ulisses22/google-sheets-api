# Google Sheets Population Tracker

This Python script allows you to fetch the current world population from an API and append it to a Google Sheets document for tracking purposes. It runs in a loop with retry logic to ensure data is updated reliably.

Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system.
- Access to a Google account.
- Access to the RapidAPI platform to obtain an API key for accessing the world population data.
- A Google Sheets document set up with appropriate headers for population count and timestamp.

### Setup

- Install the required Python packages:
`pip install gspread oauth2client requests`
- Obtain the Google Sheets credentials JSON file (YOUR_FILE.json by default) and place it in the same directory as the script.

### Set up environment variables for the following:

- GOOGLE_SHEETS_CREDS_FILE: Path to the Google Sheets credentials JSON file.
- SPREADSHEET_NAME: Name of the Google Sheets document.
- API_ENDPOINT: URL of the API endpoint to fetch world population data (RapidAPI: [https://docs.rapidapi.com/]).
- RAPIDAPI_KEY: Your RapidAPI key for accessing the world population API.

### Usage
Run the script using Python:
`python population_tracker.py`

The script will fetch the world population data, append it to the specified Google Sheets document along with a timestamp, and handle any errors gracefully with retry logic.

### Logging

The script logs errors and informational messages to a file named error.log in the script's directory. Check this log file for troubleshooting and monitoring purposes.

### Note

- Ensure the Google Sheets document is shared with the email address associated with the credentials JSON file.
- Adjust the retry attempts and delay as needed for your use case.

#### License

This project is licensed under the MIT License. See the LICENSE file for details.
