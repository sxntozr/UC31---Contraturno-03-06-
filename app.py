from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro", methods=["POST"])
def cadastro():

    nome = request.form["nome"].strip().title()
    email = request.form["email"].strip().lower()
    telefone = request.form["telefone"].strip()
    cpf = request.form["cpf"].strip()
    cidade = request.form["cidade"].strip().title()
    estado = request.form["estado"].strip().upper()
    curso = request.form["curso"].strip()
    idade = request.form["idade"].strip()
    senha = request.form["senha"].strip()

if __name__ == "__main__":
    app.run(debug=True)