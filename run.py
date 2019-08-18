from flask import Flask


app = Flask(__name__)


@app.route("/<name>",methods=['GET', 'POST'])
def aloha(name):
    return f"Alo Ha Mundo {name}"

if __name__ == "__main__":
    app.run(debug=True)