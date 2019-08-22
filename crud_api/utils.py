from models import Pessoa, Atividade, db_session, Usuarios


def insere_pessoa():
    pessoa = Pessoa(nome='TNX', idade=14)
    print(pessoa)
    pessoa.save()


def consulta_pessoa():
    pessoas = Pessoa.query.all()
    # for pessoa in pessoas:
    #    print(pessoa.nome)
    print(pessoas)
    #pessoa = Pessoa.query.filter_by(nome='TNX').first()
    # for p in pessoa:
    #    print(pessoa.nome)
    #print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade}")


def altera_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Tarcísio').first()
    pessoa.idade = 401
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoa.query.filter_by(nome='TNX').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    print(usuario)
    usuario.save()


def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # insere_pessoa()
    # altera_pessoa()
    # consulta_pessoa()
    # exclui_pessoa()
    # consulta_pessoa()
    insere_usuario('Tarcísio', 321)
    insere_usuario('tarcnux', '123')
    consulta_usuarios
