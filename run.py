from flask import Flask, render_template, url_for, request

#import sys
#sys.path.append('../')
import homenail_bd

app = Flask(__name__)


@app.route('/')
def index():

    cpf = request.args.get('cpf')
    senha = request.args.get('senha')
    retorno = homenail_bd.login(cpf, senha)

    if retorno:
        return render_template('agendamento.html', cpf = cpf, senha = senha)

    return render_template('index.html', cpf = cpf, senha = senha)


@app.route('/agendamento/')
def agendamento():
    # cpf = request.args.get('cpf')
    # senha = request.args.get('senha')
    # nome = homenail_bd.login(cpf, senha)
    # print(nome)
    return render_template('agendamento.html')


@app.route('/cadastrar_cliente/')
def cadastrar_cliente():

    retorno = ''

    nome = request.args.get('nome')
    cpf = request.args.get('cpf')
    senha = request.args.get('senha')
    telefone = request.args.get('telefone')
    cep = request.args.get('cep')
    rua = request.args.get('rua')
    numero = request.args.get('numero')
    cidade = request.args.get('cidade')
    estado = request.args.get('estado')

    if nome:
        retorno = homenail_bd.cliente(nome, cpf, senha, telefone, cep, rua, numero, cidade, estado)
        
    if retorno:
        return render_template('index.html')    
        
    return render_template('cadastrar_cliente.html')

   

if __name__ == '__main__':
    app.run(debug=True) 
    