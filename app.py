from pymongo import MongoClient
import os
from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "api.json")

@app.route("/")
def home():
    return jsonify({"message": "Flask app running successfully!"})

@app.route("/api", methods=["GET"])
def get_api_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"error": "api.json not found"}), 404

@app.route("/submittodoitem", methods=["POST"])
def submit_item():
    payload = request.get_json()
    return jsonify({
        "ok": True,
        "itemName": payload.get("itemName"),
        "itemDescription": payload.get("itemDescription")
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


<<<<<<< HEAD
# --- Mongo init (uses MONGO_URI env or defaults) ---
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/flask_todo")
_mclient = MongoClient(MONGO_URI)
_mdb = _mclient.get_default_database() if "/" in MONGO_URI.split("//",1)[-1] else _mclient["flask_todo"]
_items = _mdb["items"]

@app.post("/submittodoitem")
def submit_todo_item():
    """
    Expects JSON:
    { "itemName": "...", "itemDescription": "..." }
    Stores in MongoDB collection 'items'.
    """
    payload = (request.get_json(silent=True) or {})
    name = payload.get("itemName")
    desc = payload.get("itemDescription", "")
    if not name:
        return jsonify({"ok": False, "error": "itemName is required"}), 400

    doc = {"itemName": name, "itemDescription": desc}
    res = _items.insert_one(doc)
    return jsonify({"ok": True, "id": str(res.inserted_id), "item": doc}), 201
=======
from flask import render_template
@app.get("/todo")
def todo_page():
    return render_template("todo.html")

>>>>>>> master_1
