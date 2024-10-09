from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
 nome = "Alysson"
 dados = {
  "profissao": "Cientista de Dados",
  "salario": "R$ 8.000,00"
 }
 return render_template("index.html", nome = nome, dados = dados)


@app.route("/contato")
def contato():
 nome = "Alysson"
 return render_template("contato.html", nome = nome)

