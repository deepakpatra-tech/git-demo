from flask import Flask, jsonify

# Create Flask app instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    Simple endpoint that returns JSON with status code 200.
    """
    response_data = {
        "message": "Hello, Flask!",
        "status": "success",
        "code": 200
    }
    # jsonify automatically sets Content-Type to application/json
    return jsonify(response_data), 200

if __name__ == '__main__':
    # Run the app on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
