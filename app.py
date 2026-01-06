from flask import Flask,jsonify
ap=Flask(__name__)
@ap.route("/status")
def status():
	return jsonify({"msg": "i am okay"})
if __name__ == "__main__":
    ap.run()