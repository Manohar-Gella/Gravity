from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Process the incoming message and generate a response
    response_message = "Hello, I'm your WhatsApp bot!"

    # Send the response back to the user
    return jsonify({"message": {"body": response_message}})

if __name__ == '__main__':
    app.run(port=5000)
