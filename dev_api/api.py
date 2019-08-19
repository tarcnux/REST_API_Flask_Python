from flask import Flask
from flask_restful import Resource, Api

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

    def put(self):
        return {'Alo': 'Ha PUT'}

    def delete(self):
        return {'Alo': 'Ha DELETE'}


class Tarcnux(Resource):
    def get(self):
        return {'Alo': 'Ha Tarcnux'}


api.add_resource(Tarcnux, '/')
api.add_resource(Desenvolvedor, '/v2/dev/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
