import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from datetime import datetime
import logging
import time

# Define logging configuration
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_file = os.getenv('GOOGLE_SHEETS_CREDS_FILE', 'YOUR_GOOGLE_SHEETS_CREDS_FILE.json')
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet
spreadsheet_name = os.getenv('SPREADSHEET_NAME', 'World Population Data')
sheet = client.open(spreadsheet_name).sheet1

# Define API endpoint URL
api_endpoint = os.getenv('API_ENDPOINT', 'https://get-population.p.rapidapi.com/population')
api_key = os.getenv('RAPIDAPI_KEY', 'YOUR_KEY')

# Fetch world population data
def get_world_population():
    try:
        response = requests.get(api_endpoint, headers={"X-RapidAPI-Key": api_key})
        response.raise_for_status() 
        data = response.json()
        population = data.get('count')
        logging.info(f"Successfully fetched world population: {population}")
        return population
    except Exception as e:
        logging.error(f"Error fetching world population data: {e}")
        return None

# Function to append data to Google Spreadsheet
def update_spreadsheet():
    population = get_world_population()
    if population is not None:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sheet.append_row([population, timestamp])
    else:
        logging.warning("Skipping update due to error fetching population data")

# Main function
def main():
    update_attempts = 0
    max_attempts = 3
    while update_attempts < max_attempts:
        update_attempts += 1
        try:
            update_spreadsheet()
            break
        except Exception as e:
            logging.error(f"Error updating spreadsheet: {e}")
            logging.info(f"Retrying update in {2**update_attempts} seconds...")
            time.sleep(2**update_attempts)
    else:
        logging.error(f"Failed to update spreadsheet after {max_attempts} attempts")

if __name__ == "__main__":
    main()
