from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

def reorder_user_data(user_data):
    return {
        "username": user_data["username"],
        "name": user_data["name"],
        "age": user_data["age"],
        "city": user_data["city"]
    }

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(reorder_user_data(user))
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    if not user_data.get('username'):
        return jsonify({"error": "Username not provided"}), 400
    username = user_data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run(debug=True)
