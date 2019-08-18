# REST_API_Flask_Python
REST API com Flask

REST - Representational State Transfer

# [Curso de FLASK na Digital Innovation One](http://gg.gg/digitalinnovation)
18/08/2019

## Criação de Ambiente Virtual
 `python -m venv env_flask`
 `env_flask\Scripts\activate`

 `pip install flask`

 `pip freeze > requirements.txt`
 `pip install -r requirements.txt`


## Rota para a primeira aplicação
 http://127.0.0.1:5000/Tarcnux

## Para reiniciar o server automaticamente
`app.run(debug=True)`

## mysqlclient
Para a instalação do mysqlclient é necessário a instalação do [*Microsoft Build Tools 2015*](https://www.microsoft.com/en-us/download/details.aspx?id=48159)

*Mas só isso não foi o suficiente para conseguir instalar.*

### install using wheel

`pip install wheel`
download from http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python

For python 3.x:
`pip install mysqlclient-1.4.3-cp37-cp37m-win_amd64.whl`
cp37 significa CPython 3.7

For python 2.7:
`pip install mysqlclient-1.3.8-cp27-cp27m-win_amd64.whl`
