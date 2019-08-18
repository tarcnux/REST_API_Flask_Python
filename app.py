from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def api():
    return jsonify({'nome': 'Tarcísio Nunes'})

if __name__ == "__main__":
    app.run(debug=True)