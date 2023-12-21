from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)  # Define the Flask app here

# Replace 'your_api_key_here' with the actual API key
#API_KEY = os.environ.get('BODYGRAPH') #, 'your_api_key_here'
API_KEY = os.getenv("BODYGRAPH"), 

#@app.route('/')
#def home():
#    return "Welcome to my Flask app!"

# The route that your users will call
@app.route('/fetch-bodygraph-data', methods=['GET'])
def fetch_bodygraph_data():
    # Fetch parameters from the incoming request
    date = request.args.get('date')
    timezone = request.args.get('timezone')

    url = "https://api.bodygraphchart.com/v221006/hd-data"
    payload = {
        'api_key': API_KEY,
        'date': date,
        'timezone': timezone
    }

    # Make a request to the original API
    response = requests.get(url, params=payload)

    # Return the response as JSON
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data", "status_code": response.status_code})

#if __name__ == '__main__':
    # Only run the app if this script is executed directly
#    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
#    app.run(host='0.0.0.0', port=port, debug=True)  # Start the Flask app


if __name__ == '__main__':
    app.run(debug=True)