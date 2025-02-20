from Flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app is running on Render!"

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    user_input = data.get("text", "")
    return jsonify({"message": f"You entered: {user_input}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
