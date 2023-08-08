from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your API endpoint URL
API_URL = "https://api.example.com/forex"

@app.route('/get_forex_data', methods=['GET'])
def get_forex_data():
    try:
        currency_pair = request.args.get('pair', 'EURUSD')
        response = requests.get(f"{API_URL}/{currency_pair}")
        
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": "Failed to fetch data from API"}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
