import pandas as pd
import requests

# Define the API endpoint
api_url = "https://restcountries.com/v3.1/all"

# Send a GET request to the API
response = requests.get(api_url)

# Check if the request was successfully
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract country and capital information
    countries = []
    capitals = []

    for country_data in data:
        country_name = country_data["name"]["common"]
        capital = country_data.get("capital", "N/A")
        countries.append(country_name)
        capitals.append(capital)

    # Create a DataFrame
    df = pd.DataFrame({"Country": countries, "Capital": capitals})

    # Save the DataFrame to a CSV file
    df.to_csv("countries_and_capitals.csv", index=False)

    print("CSV dataset created successfully.")
else:
    print("Failed to fetch data from the API.")

