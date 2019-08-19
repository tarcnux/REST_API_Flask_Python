from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

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


class Desenvolvedor(Resource):
    '''Retorna, altera e deleta um desenvolvedor pelo ID'''

    def get(self, id):
        try:
            response = desenvolvedores[id]
            print(response)
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe."
            response = {"status": "erro", "mensagem": mensagem}
        except Exception:
            mensagem = "Erro desconhecido."
            response = {"status": "erro", "mensagem": mensagem}
        return response

    def put(self, id):
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
        return response

    def delete(self, id):
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
        return response


class Tarcnux(Resource):
    def get(self):
        return {'Alo': 'Ha Tarcnux'}


api.add_resource(Tarcnux, '/')
api.add_resource(Desenvolvedor, '/v2/dev/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
