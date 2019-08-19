from models import Pessoa, Atividade


def insere_pessoa():
    pessoa = Pessoa(nome='Tarcnux', idade=41)
    print(pessoa)


def consulta():
    pass


if __name__ == '__main__':
    insere_pessoa()
