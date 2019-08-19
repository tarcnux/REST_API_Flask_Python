from models import Pessoa, Atividade, db_session


def insere_pessoa():
    pessoa = Pessoa(nome='TNX', idade=14)
    print(pessoa)
    pessoa.save()


def consulta_pessoa():
    #pessoas = Pessoa.query.all()
    # for pessoa in pessoas:
    #    print(pessoa.nome)

    pessoa = Pessoa.query.filter_by(nome='Tarcísio').first()
    # for p in pessoa:
    #    print(pessoa.nome)
    print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade}")


if __name__ == '__main__':
    # insere_pessoa()
    consulta_pessoa()
