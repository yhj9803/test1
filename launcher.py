from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def index():
	return jsonify(result="hello!2222")
if __name__ == "__main__":
	app.run("0.0.0.0", port=5000)