from flask import Flask, render_template, url_for, request, redirect, url_for, session

from models import Cliente, Fornecedor, Agendamento, Login
#import sys
#sys.path.append('../')
import homenail_bd

app = Flask(__name__)
app.secret_key = 'Fatec_ython'


@app.route('/')
def index():
    print('run - index')
    return render_template('index.html')


@app.route('/cadastrar_cliente', methods=['POST',])
def cadastrar_cliente():
    print('run - cadastrar_cliente')
    return render_template('cadastrar_cliente.html')

@app.route('/cadastrar_cliente_banco', methods=['POST',])
def cadastrar_cliente_banco():
    print('run - cadastrar_cliente_banco')

    cliente = Cliente(nome=request.form['nome'],
                      cpf=int(request.form['cpf']),
                      senha=request.form['senha'],
                      telefone=int(request.form['telefone']),
                      cep=int(request.form['cep']),
                      rua=request.form['rua'],
                      numero=int(request.form['numero']),
                      cidade=request.form['cidade'],
                      estado=request.form['estado'])

    if cliente:
        retorno = homenail_bd.cadastrar_cliente(cliente) 

    return render_template('index.html')
    

@app.route('/cadastrar_fornec')
def cadastrar_fornec():
    print('run - cadastrar_fornec')
    # if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #     return redirect(url_for('index'))
    return render_template('cadastrar_fornec.html')


@app.route('/consulta_agendamentos_cliente')
def consulta_agendamentos_cliente():
    print('run - consulta_agendamentos_cliente')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('consulta_agendamentos_cliente.html')


@app.route('/consulta_agendamentos_fornec')
def consulta_agendamentos_fornec():
    print('run - consulta_agendamentos_fornec')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('consulta_agendamentos_fornec.html')


@app.route('/criar_agendamento')
def criar_agendamento():
    print('run - criar_agendamento')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('criar_agendamento.html')


@app.route('/editar_agendamento')
def editar_agendamento():
    print('run - editar_agendamento')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('editar_agendamento.html')


@app.route('/editar_cadastro_cliente')
def editar_cadastro_cliente():
    print('run - editar_cadastro_cliente')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('editar_cadastro_cliente.html')


@app.route('/editar_cadastro_fornec')
def editar_cadastro_fornec():
    print('run - editar_cadastro_fornec')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('editar_cadastro_fornec.html')

@app.route('/sobre')
def sobre():
    print('run - sobre')
    return render_template('sobre.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    print('run - autenticar')
    
    login = Login(cpf=request.form['cpf'], 
                  senha=request.form['senha'])
 
    if len(login.cpf) == 11:
        session['tipo'] = 'cliente'
        retorno = homenail_bd.login_cliente(login)

        if retorno:
            session['usuario_logado'] = login.cpf
            return redirect(url_for('consulta_agendamentos_cliente'))
        else:
            return redirect(url_for('index'))

    elif len(login.cpf) == 14:
        session['tipo'] = 'fornec'
        return redirect(url_for('consulta_agendamentos_fornec'))

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    print('run - logout')

    session['usuario_logado'] = None
    # flash('Nenhum Usuário logado!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 
    