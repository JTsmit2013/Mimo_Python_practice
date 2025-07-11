import requests

# Function to fetch data from the SWAPI based on a given category (option)
def fetch_data(option):
    url = f"https://swapi.mimo.dev/api/{option}/"
    data = []

    # Try to make a GET request to the API and handle HTTP errors
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()       # Parse the JSON response into a Python object
        print(f"Successfully fetched {len(data)} entities")
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None

    return data

# Prompt the user to choose a category of Star Wars data to retrieve
option = input(
    'What Star Wars information do you want? ("people", "planets", "starships", "vehicles", "species", or "films"): '
).strip().lower()

# Fetch the data from the selected category
data = fetch_data(option)

# Display each entity's name if data was successfully retrieved
if data:
    for entity in data:
        print(entity['name'])
else:
    print("Unable to download data")
