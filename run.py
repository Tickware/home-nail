from flask import Flask, render_template, url_for, request, redirect, url_for, session

#import sys
#sys.path.append('../')
import homenail_bd

app = Flask(__name__)
app.secret_key = 'Fatec_ython'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar_cliente', methods=['POST',])
def cadastrar_cliente():

    retorno = ''

    nome = request.form['nome']
    cpf = request.form['cpf']
    senha = request.form['senha']
    telefone = request.form['telefone']
    cep = request.form['cep']
    rua = request.form['rua']
    numero = request.form['numero']
    cidade = request.form['cidade']
    estado = request.form['estado']

    if nome:
        retorno = homenail_bd.cliente(nome, cpf, senha, telefone, cep, rua, numero, cidade, estado)
        
    if retorno:
        return redirect(url_for('index'))

        
    return render_template('cadastrar_cliente.html')


@app.route('/cadastrar_fornec')
def cadastrar_fornec():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('cadastrar_fornec.html')


@app.route('/consulta_agendamentos_cliente')
def consulta_agendamentos_cliente():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('consulta_agendamentos_cliente.html')


@app.route('/consulta_agendamentos_fornec')
def consulta_agendamentos_fornec():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('consulta_agendamentos_fornec.html')


@app.route('/criar_agendamento')
def criar_agendamento():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('criar_agendamento.html')


@app.route('/editar_agendamento')
def editar_agendamento():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('editar_agendamento.html')


@app.route('/editar_cadastro_cliente')
def editar_cadastro_cliente():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('editar_cadastro_cliente.html')


@app.route('/editar_cadastro_fornec')
def editar_cadastro_fornec():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    return render_template('editar_cadastro_fornec.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():

    cpf = request.form['cpf']
    senha = request.form['senha']
 
    if len(cpf) == 11:
        session['tipo'] = 'cliente'

        retorno = homenail_bd.login_cliente(int(cpf), senha)

        if retorno:
            session['usuario_logado'] = request.form['cpf']
            return redirect(url_for('consulta_agendamentos_cliente'))
        else:
            return redirect(url_for('index'))

    elif len(cpf) == 14:
        session['tipo'] = 'fornec'
        return redirect(url_for('consulta_agendamentos_fornec'))

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    # flash('Nenhum Usuário logado!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 
    