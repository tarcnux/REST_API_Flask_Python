from models import Pessoa, Atividade


def insere_pessoa():
    pessoa = Pessoa(nome='Tarcnux', idade=41)
    print(pessoa)


def consulta():
    pessoa = Pessoa.query.filter_by(nome='Tarcnux')
    print(pessoa)


if __name__ == '__main__':
    # insere_pessoa()
    consulta()
