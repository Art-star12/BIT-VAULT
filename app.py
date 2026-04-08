from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "BIT-VAULT Backend is Running - AES-256 Protocol Active"

@app.route('/scan')
def scan():
    # Placeholder for YARA rule logic
    return jsonify({"status": "ready", "engine": "Sentinel AI"})

if __name__ == '__main__':
    app.run(debug=True)
