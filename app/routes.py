from app import app
from flask import render_template
# pacote para recuperar info de formulario
from flask import request

#Pacote para mensagens Flash (senha incorreta etc)
from flask import flash

# import para redirecionar
from flask import redirect

@app.route("/", defaults={"nome":"Usuário"})
@app.route("/index", defaults={"nome":"Usuário"})
@app.route("/index/<nome>")
def index(nome):
 dados = {
  "profissao": "Cientista de Dados",
  "salario": "R$ 8.000,00"
 }
 return render_template("index.html", nome = nome, dados = dados)


@app.route("/contato")
def contato():
 nome = "Alysson"
 return render_template("contato.html", nome = nome)


@app.route("/login")
def login():
 return render_template("login.html")

# Definindo que a rota aceita o tipo get e POST
@app.route("/autenticar", methods = ['POST'])
def autenticar():
 # usuario = request.args.get("usuario")
 # texto = request.args.get("texto")
 # senha = request.args.get("senha")

 usuario = request.form.get("usuario")
 texto = request.form.get("texto")
 senha = request.form.get("senha") 
 if usuario == 'admin' and senha == 'senha123':
  return f"Usuário: {usuario}\
   \nSenha: {senha}\
   \nTexto: {texto}"

 else:
  flash("Dados Inválidos")
  return redirect('/login')