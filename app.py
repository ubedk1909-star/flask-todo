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


from flask import render_template
@app.get("/todo")
def todo_page():
    return render_template("todo.html")

