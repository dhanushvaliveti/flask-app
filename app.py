from flask import Flask, jsonify, request

app = Flask(__name__)
users = []

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if data is None or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    user = {
        "id": len(users) + 1,
        "name": data["name"]
    }
    users.append(user)
    return jsonify(user), 201


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if data is None or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return "", 204
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)






