from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if data is None or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    user = User(name=data["name"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"id": user.id, "name": user.name}), 201


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(
        [{"id": user.id, "name": user.name} for user in users]
    ), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"id": user.id, "name": user.name}), 200


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if data is None or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    user.name = data["name"]
    db.session.commit()

    return jsonify({"id": user.id, "name": user.name}), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
