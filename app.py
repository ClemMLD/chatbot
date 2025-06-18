from flask import Flask, request, jsonify, os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

app.run(host='0.0.0.0', port=port)

@app.route('/')
def home():
    return "Welcome to the Chatbot API!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = f"You said:{user_message}"
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
