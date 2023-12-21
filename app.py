from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)  # Define the Flask app here

API_KEY = os.getenv("BODYGRAPH")#, 'your_api_key_here'

@app.route('/')
def home():
    return "Welcome to my Flask app!"

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

    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()  # This will raise an exception for HTTP errors
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:", errh)
        return jsonify({"error": str(errh), "status_code": 500})
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
        return jsonify({"error": str(errc), "status_code": 500})
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
        return jsonify({"error": str(errt), "status_code": 500})
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else", err)
        return jsonify({"error": str(err), "status_code": 500})

if __name__ == '__main__':
    # Only run the app if this script is executed directly
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host='0.0.0.0', port=port, debug=True)  # Start the Flask app

