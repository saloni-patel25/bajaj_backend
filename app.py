from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for the root URL
@app.route('/')
def home():
    return "Welcome to the BFHL API. Use /bfhl for GET or POST requests."

# Route for /bfhl with GET and POST methods
@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        # Return operation code for GET request
        return jsonify({"operation_code": 1}), 200

    if request.method == 'POST':
        # Parse the JSON request body
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', None)

        # Separate numbers and alphabets
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]

        # Find the highest lowercase alphabet
        highest_lowercase = max([char for char in alphabets if char.islower()], default="")

        # Handle file validation (this is a simplified example)
        file_valid = bool(file_b64)
        file_mime_type = "image/png"  # In a real scenario, you'd detect the MIME type
        file_size_kb = 400  # Example size, in a real scenario you'd calculate this

        # Create the response data
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Example user_id
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        # Return the response
        return jsonify(response), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
