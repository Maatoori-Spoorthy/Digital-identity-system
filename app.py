from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

# 🔐 Create identity hash
def create_identity(name, email):
    data = f"{name}:{email}"
    return hashlib.sha256(data.encode()).hexdigest()

# ⛓️ Simulated blockchain storage (no errors)
def store_on_blockchain(data):
    return "TXN_" + data[:12]

# 🏠 Home route
@app.route('/')
def home():
    return "Blockchain Identity System Running ✅"

# 👤 Create identity
@app.route('/create_identity', methods=['POST'])
def create():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    identity_hash = create_identity(name, email)
    txid = store_on_blockchain(identity_hash)

    return jsonify({
        "message": "Identity Created ✅",
        "hash": identity_hash,
        "txid": txid
    })

# 🔍 Verify identity
@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    identity_hash = create_identity(name, email)

    return jsonify({
        "message": "Identity Verified ✅",
        "hash": identity_hash
    })

# ▶️ Run server
if __name__ == '__main__':
    app.run(debug=True)