from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/<int:id>")
def api(id):
    return jsonify({'id':id, 'nome': 'Tarcísio Nunes', 'profissao': 'professor'})

if __name__ == "__main__":
    app.run(debug=True)