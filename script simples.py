from flask import Flask, request
import banco_dados

app = Flask(__name__)

@app.route("/")
def home():
    return homepage()

@app.route("/contar", methods=['POST', 'GET'])
def contar():
    resultado = ""
    contagem = 0
    while contagem <= 100:
        resultado += f"<h2>teste n {contagem}</h2>"
        contagem += 1
    return resultado
    
def homepage():
    pagina = "<h1>Bem-vindo ao site!</h1>" \
    "<br>" \
    "<h3>Cadastre seu nome no banco de dados</h3>" \
    "<form name='formcadastro' action='/cadastrar' method='POST'>" \
    "<input type='text' name='nome'>" \
    "<input type='submit'>" \
    "</form>"
    return pagina

@app.route("/cadastrar", methods=['POST'])
def cadastrarNome():
    if request.method == 'POST':
        banco_dados.registrarNome(request.form['nome'])
        return "Nome cadastrado"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)