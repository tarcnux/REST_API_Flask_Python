from models import Pessoa, Atividade, db_session


def insere_pessoa():
    pessoa = Pessoa(nome='Tarcnux', idade=41)
    print(pessoa)
    db_session.add(pessoa)
    db_session.commit()


def consulta():
    pessoa = Pessoa.query.all()
    print(pessoa)


if __name__ == '__main__':
    # insere_pessoa()
    consulta()
