import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
client = MongoClient("MONGO_URI")
db = client.todo

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

@app.route("/submittodoitem", methods=["POST"])
def submit_item():
    item = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription")
    }
    db.items.insert_one(item)
    return "Saved!"

#try

if __name__ == "__main__":
    app.run(debug= True) 