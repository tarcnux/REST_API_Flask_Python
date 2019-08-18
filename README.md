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

## Para reiniciar o server automaticamente
`app.run(debug=True)`

No terminal: py .\app.py

## Rota para a primeira aplicação
 http://127.0.0.1:5000/

# JSON API
## Passando Json no Postman
Endpoint: http://127.0.0.1:5000/somav2

**Body raw JSON**

{ "valores": [1, 2, 3, 4, 5, 6, 7, 8, 9] }

## Passando Json com requests (não confundir com a flask requests)
### Simulando a interação entre aplicações
No terminal digite python. 
>>> import requests

### Método GET

>>> response = requests.get('http://127.0.0.1:5000/10')
>>> print(response.text)
>>> print(response.json())
>>> dados = response.json()
>>> print(f"Nome: {dados['nome']} - Profissão: {dados['profissao']}")

### Método POST
>>> import json
>>> response = requests.post('http://127.0.0.1:5000/somav2', json={'valores':[10,20,30,40,50,60,70,80,90]})
>>> print(response.json())
>>> dados = response.json()
>>> print(f"Soma = {dados['soma']}")

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
