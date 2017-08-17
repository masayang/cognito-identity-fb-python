from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/guest/hello")
def public_hello():
    return jsonify({
        "greeting": "Hello",
        "message": "This is an opened API."
    })


@app.route("/authorized/hello")
def authorized_hello():
    return jsonify({
        "greeting": "Hello, Authorized User!",
        "message": "This is a restricted API. Thank you for signing-in."
    })
