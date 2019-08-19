from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'Fask',
                     'PHP', 'Django', 'JTML', 'CSS', 'JS']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades
