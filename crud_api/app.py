from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoa


app = Flask(__name__)
api = Api(app)


class PessoaFlask(Resource):
    def get(self, nome):
        '''Busca no banco de dados'''
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response

    def put(self, nome):
        '''Alteração de nome e idade'''
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response


api.add_resource(PessoaFlask, '/pessoa/<string:nome>/')

if __name__ == '__main__':
    app.run(debug=True)
