from flask import Flask, request, jsonify
import requests
import os

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)

app = Flask(__name__)

# Replace 'your_api_key_here' with the actual API key
API_KEY = os.environ.get('BODYGRAPH', 'your_api_key_here')

# The route that your users will call
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Extract parameters from the request
    date = request.args.get('date')
    timezone = request.args.get('timezone')

    # Validate inputs
    if not date or not timezone:
        return jsonify({"error": "Missing date or timezone"}), 400

    # Prepare the payload for the original API
    payload = {
        'api_key': API_KEY,
        'date': date,
        'timezone': timezone
    }

    # Make a request to the original API
    response = requests.post('https://api.bodygraphchart.com/v221006/hd-data', data=payload)

    # Check if the request was successful
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data from the original API"}), 500

    # Return the data received from the original API
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
