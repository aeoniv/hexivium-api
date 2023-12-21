import requests

# The API endpoint you're trying to access
url = 'https://hexivium-api-f8562e921bd9.herokuapp.com/fetch-data'


# Your API key and other parameters
api_key = 'your_api_key'
date = '2019-05-05 10:10'
timezone = 'Europe/London'

# Prepare your request parameters
params = {
    'api_key': api_key,
    'date': date,
    'timezone': timezone
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data: {response.status_code}")

# Handle the data as needed
# For example, you can print it, process it, or save it to a file
