from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load environment variables from .evn file
load_dotenv()

# Access SECRET_KEY environment variable
secret_key = os.getenv("SECRET_KEY")

# POST endpoint to receive and print POST data


# POST endpoint to receive GitHub webhook events
@app.route('/hook', methods=['POST'])
def github_webhook():
    data = request.get_json()

    if data:
        print("Received GitHub webhook payload:")
        print(data)
        return "Webhook received successfully!"
    else:
        return "No data received."

@app.route('/receive_post_data', methods=['POST'])
def receive_post_data():
    data = request.get_json()  # assuming JSON data in the POST request
    print(f"Received POST data: {data}")
    return "POST data received successfully!"

# GET endpoint to provide a sample response


@app.route('/sample_get_endpoint', methods=['GET'])
def sample_get_endpoint():
    response = {"message": "Hello, this is a sample GET endpoint!"}
    return jsonify(response)


if __name__ == '__main__':
    # Bind to '0.0.0.0' to make it accessible externally
    # Use a specific port, for example, 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
