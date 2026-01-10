from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route("/")
def hello():
    return jsonify({"hello":"i am dhanush"})
@app.route("/status")
def status():
	return jsonify({"status": "i am okay"})
@app.route("/echo",methods=["POST"])
def echo():
    data=request.get_json()
    if data is None:
        return jsonify({"error": "No JSON received"}), 400
    return jsonify(data)
@app.route("/sum",methods=["POST"])
def sum():
    data=request.get_json()
    if data is None:
        return jsonify({"errror":"no json recieved"}),400
    if "a" not in data or "b" not in data:
        return jsonify({"errror":"no json recieved"}),400
    result=data["a"]*data["b"]
    return jsonify({"result":result})
if __name__ == "__main__":
    app.run()


