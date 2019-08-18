from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/")
def aloha():
    return "Alo Ha dev_api"


if __name__ == "__main__":
    app.run(debug=True)
