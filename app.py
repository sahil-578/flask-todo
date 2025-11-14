from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/api")
def api():
    data = {
        "message" : "Initial JSON data",
        "version" : 2}    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug= True) 