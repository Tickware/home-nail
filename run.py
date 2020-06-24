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
    print (retorno)
    return render_template('index.html', cpf = cpf, senha = senha)

if __name__ == '__main__':
    app.run(debug=True) 