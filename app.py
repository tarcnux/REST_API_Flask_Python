from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/<int:id>")
def api(id):
    return jsonify({'id': id, 'nome': 'Tarcísio Nunes', 'profissao': 'professor'})


@app.route("/soma/<int:inteiro1>/<int:inteiro2>", methods=['POST'])
def soma(inteiro1, inteiro2):
    return jsonify({
        'inteiro1': inteiro1,
        'inteiro2': inteiro2,
        'soma': inteiro1+inteiro2
    })


if __name__ == "__main__":
    app.run(debug=True)
