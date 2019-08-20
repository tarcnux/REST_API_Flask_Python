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
        try:
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
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response

    def delete(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        try:
            pessoa.delete()
            mensagem = f"Pessoa {pessoa.nome} excluída com sucesso."
            response = {'status': 'sucesso', 'mensagem': mensagem}
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response


class ListaPessoasFlask(Resource):
    def get(self):
        pessoas = Pessoa.query.all()
        response = [{"id": pessoa.id,
                     "nome": pessoa.nome,
                     "idade": pessoa.idade
                     } for pessoa in pessoas]
        return response


class InserePessoaFlask(Resource):
    def post(self):
        dados = request.json
        pessoa = Pessoa(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


api.add_resource(PessoaFlask, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoasFlask, '/pessoas/')
api.add_resource(InserePessoaFlask, '/pessoa/')

if __name__ == '__main__':
    app.run(debug=True)
