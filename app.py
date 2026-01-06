from flask import Flask,jsonify
app=Flask(__name__)
@app.route("/status")
def hello():
	return jsonify({"msg": "hello"})
if __name__ == "__main__"
    app.run(debug=True)

