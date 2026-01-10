from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "i am dhanush"})

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON received"}), 400
    return jsonify(data)

@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON received"}), 400

    if "a" not in data or "b" not in data:
        return jsonify({"error": "Missing a or b"}), 400

    return jsonify({"result": data["a"] + data["b"]})

if __name__ == "__main__":
    app.run(debug=True)




