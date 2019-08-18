from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

desenvolvedores = [
    {"id": 0,
        "nome": "Tarcísio Nunes",
        "habilidades": ["Python", "Flask", "PHP", "MySQL", "HTML", "CSS"]},
    {"id": 1,
        "nome": "Tarcnux TNX",
        "habilidades": ["Python", "Django"]},
    {"id": 2,
        "nome": "Guido van Rossum",
        "habilidades": ["Python", "Django", "Flask"]}
]


@app.route('/v1/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    '''Permite registrar um novo desenvolvedor e lista todos desenvovedores'''
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == "GET":
        return jsonify(desenvolvedores)


@app.route("/v1/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    '''Retorna, altera e deleta um desenvolvedor pelo ID'''
    response = ""
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
            print(response)
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe."
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido."
            response = {"status": "erro", "mensagem": mensagem}
    elif request.method == "PUT":
        dados = json.loads(request.data)
        try:
            desenvolvedores[id] = dados
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe."
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido."
            response = {"status": "erro", "mensagem": mensagem}
    elif request.method == "DELETE":
        try:
            desenvolvedores.pop(id)
            response = {"status": "sucesso",
                        "mensagem": "Registro " + str(id) + " excluído."}
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe."
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido."
            response = {"status": "erro", "mensagem": mensagem}
    return jsonify(response)


@app.route("/", methods=["GET", "POST"])
def aloha():
    return "Alo HA!"


if __name__ == "__main__":
    app.run(debug=True)
