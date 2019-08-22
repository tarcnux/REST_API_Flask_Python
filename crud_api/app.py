from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoa, Atividade, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'tarcnux': '123',
#     'tnx': '321'
# }


# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class PessoaFlask(Resource):
    @auth.login_required
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


class ListaAtividadesFlask(Resource):
    def get(self):
        atividades = Atividade.query.all()
        response = [{"id": atividade.id,
                     "nome": atividade.nome,
                     "pessoa": atividade.pessoa.nome
                     } for atividade in atividades]
        return response


class InsereAtividadeFlask(Resource):
    def post(self):
        dados = request.json
        pessoa = Pessoa.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividade(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(PessoaFlask, '/v1/pessoa/<string:nome>/')
api.add_resource(ListaPessoasFlask, '/v1/pessoas/')
api.add_resource(InserePessoaFlask, '/v1/pessoa/')
api.add_resource(InsereAtividadeFlask, '/v1/atividade/')
api.add_resource(ListaAtividadesFlask, '/v1/atividades/')
# api.add_resource(AtividadeFlask, '/v1/atividade/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
