from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
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


class ListaDesenvolvedores(Resource):
    '''Permite registrar um novo desenvolvedor e lista todos desenvovedores'''

    def get(self):
        '''Exibe lista de todos desenvolvedores'''
        return desenvolvedores

    def post(self):
        '''Insere um novo desenvolvedor no final da lista'''
        dados = json.loads(request.data)
        tamanho = len(desenvolvedores)
        # Incrementa o último id
        posicao = int(desenvolvedores[tamanho-1]["id"])+1
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[tamanho]


class Desenvolvedor(Resource):
    '''Retorna, altera e deleta um desenvolvedor pelo ID'''

    def get(self, id):
        '''Se existir, retorna um desenvolvedor'''
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
        '''Se existir, altera dados de um desenvolvedor'''
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
        '''Se existir, exclui um desenvolvedor'''
        global desenvolvedores
        try:
            # desenvolvedores.pop(id)
            existe = [i for i in desenvolvedores if (i['id'] == id)]
            if not existe:
                raise IndexError
            desenvolvedores = [
                i for i in desenvolvedores if not (i['id'] == id)]
            response = {"status": "sucesso",
                        "mensagem": "Registro " + str(id) + " excluído."}
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe."
            response = {"status": "erro", "mensagem": mensagem}
        except Exception as e:
            #mensagem = "Erro desconhecido."
            response = {"status": "erro", "mensagem": str(e)}
        return response


class Tarcnux(Resource):
    def get(self):
        return {'Alo': 'Ha Tarcnux'}


# Rotas
api.add_resource(Tarcnux, '/')
api.add_resource(Desenvolvedor, '/v2/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/v2/dev/')
api.add_resource(Habilidades, '/v2/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
