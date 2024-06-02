#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"},
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"}}


@app.route('/')
def home():
    """
    Handle the root URL route and provide a welcome message.

    Returns:
            str: A welcome message to be displayed at the root URL.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    Provide a list of all usernames stored in the system.

    Returns:
            A JSON response containing a list of all usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Check the status of the API and return a simple message.

    Returns:
            str: A status message indicating the API is running.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Fetch and return user details for a given username.

    Args:
            username: The username whose details are to be retrieved.

    Returns:
            If the user exists, return their details as a JSON response.
            If the user does not exist, return an error message
            and a 404 status code.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the system with the provided details.

    Returns:
            A JSON response with a confirmation message
            and user details if successful.
            If the username is missing or already exists,
            return an appropriate error message.
    """
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
