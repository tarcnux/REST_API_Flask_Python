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
    def get(self):
        return {'Alo': 'Ha GET'}

    def put(self):
        return {'Alo': 'Ha PUT'}

    def delete(self):
        return {'Alo': 'Ha DELETE'}


class Tarcnux(Resource):
    def get(self):
        return {'Alo': 'Ha Tarcnux'}


api.add_resource(Tarcnux, '/')
api.add_resource(Desenvolvedor, '/v2/dev/')

if __name__ == '__main__':
    app.run(debug=True)
