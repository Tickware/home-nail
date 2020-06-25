from flask import Flask, render_template, url_for, request

#import sys
#sys.path.append('../')
import homenail_bd

app = Flask(__name__)

@app.route('/')
def index():
    cpf = request.args.get('cpf')
    senha = request.args.get('senha')
    print(cpf)
    retorno = homenail_bd.login(cpf, senha)
    print (retorno)
    if retorno:
        return render_template('agendamento.html')
    print('index')
    return render_template('index.html', cpf = cpf, senha = senha)

@app.route('/agendamento/')
def agendamento():
    return render_template('agendamento.html')

@app.route('/cadastrar/')
def cadastrar():
    print ('Cadastraaaaar')
    return render_template('cadastrar.html')

    

if __name__ == '__main__':
    app.run(debug=True) 