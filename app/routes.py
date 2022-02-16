from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    name = "Coletivo & Criativos"
    dados = {"catalogo": "Produtos", "linksUteis":"Loja"}
    return render_template('index.html')

@app.route('/atacado')
def atacado():
    name = "Coletivo & Criativos"
    dados = {"catalogo": "Produtos", "linksUteis":"Loja"}
    return render_template('atacado.html')

@app.route('/varejo')
def  varejo():
    return render_template('varejo.html')