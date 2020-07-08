from flask import Flask, render_template, url_for, request, redirect, url_for, session

from models import Cliente, Fornec, Agendamento, Login
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
        homenail_bd.cadastrar_cliente(cliente) 

    return render_template('index.html')
    

@app.route('/cadastrar_fornec', methods=['POST',])
def cadastrar_fornec():
    print('run - cadastrar_fornec')
    return render_template('cadastrar_fornec.html')


@app.route('/cadastrar_fornec_banco', methods=['POST',])
def cadastrar_fornec_banco():
    print('run - cadastrar_fornec_banco')

    fornec = Fornec(nome=request.form['nome'],
                      cnpj=int(request.form['cnpj']),
                      senha=request.form['senha'],
                      telefone=int(request.form['telefone']),
                      cidade=request.form['cidade'],
                      estado=request.form['estado'])

    if fornec:
        homenail_bd.cadastrar_fornec(fornec) 

    return render_template('index.html')


@app.route('/consulta_agendamentos_cliente')
def consulta_agendamentos_cliente():
    print('run - consulta_agendamentos_cliente')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))

    agendamentos = homenail_bd.agendamento_por_cliente(session['usuario_logado'])
    
    return render_template('consulta_agendamentos_cliente.html', agendamentos=agendamentos)


@app.route('/consulta_agendamentos_fornec')
def consulta_agendamentos_fornec():
    print('run - consulta_agendamentos_fornec')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))

    agendamentos = homenail_bd.agendamento_por_fornec(session['usuario_logado'])

    return render_template('consulta_agendamentos_fornec.html', agendamentos=agendamentos)


@app.route('/criar_agendamento', methods=['POST',])
def criar_agendamento():
    print('run - criar_agendamento')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))

    fornecs = homenail_bd.busca_dados_todos_fornec()

    return render_template('criar_agendamento.html', fornecs=fornecs)


@app.route('/criar_agendamento_banco', methods=['POST',])
def criar_agendamento_banco():
    print('run - criar_agendamento_banco')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))

    agendamento = Agendamento(cpf_cliente=session['usuario_logado'],
                              cnpj_fornec=request.form['cnpj_fornec'],
                              tp_servico=request.form['tp_servico'],
                              data=request.form['data'],
                              hora=str(request.form['hora']))

    homenail_bd.cadastrar_agendamento(agendamento)

    return redirect('consulta_agendamentos_cliente')


@app.route('/deletar_agendamento/<int:id_deletar>')
def deletar_agendamento(id_deletar):
    print('run - deletar_agendamento')
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    
    homenail_bd.deletar_agendamento(id_deletar)

    return redirect(url_for('consulta_agendamentos_cliente'))


@app.route('/editar_cadastro_cliente')
def editar_cadastro_cliente():
    print('run - editar_cadastro_cliente')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    
    cliente = homenail_bd.busca_dados_cliente(session['usuario_logado'])

    return render_template('editar_cadastro_cliente.html', cliente=cliente)


@app.route('/editar_cliente_banco', methods=['POST',])
def editar_cliente_banco():
    print('run - editar_cadastro_banco')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    
    cliente = Cliente(nome=request.form['nome'],
                      cpf=int(request.form['cpf']),
                      senha=request.form['senha'],
                      telefone=int(request.form['telefone']),
                      cep=int(request.form['cep']),
                      rua=request.form['rua'],
                      numero=int(request.form['numero']),
                      cidade=request.form['cidade'],
                      estado=request.form['estado'])

    homenail_bd.atualiza_cliente(cliente)
    
    return redirect(url_for('consulta_agendamentos_cliente'))


@app.route('/editar_cadastro_fornec')
def editar_cadastro_fornec():
    print('run - editar_cadastro_fornec')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    
    fornec = homenail_bd.busca_dados_fornec(session['usuario_logado'])

    return render_template('editar_cadastro_fornec.html', fornec=fornec)


@app.route('/editar_fornec_banco', methods=['POST',])
def editar_fornec_banco():
    print('run - editar_cadastro_banco')

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    
    fornec = Fornec(nome=request.form['nome'],
                    cnpj=int(request.form['cnpj']),
                    senha=request.form['senha'],
                    telefone=int(request.form['telefone']),
                    cidade=request.form['cidade'],
                    estado=request.form['estado'])

    homenail_bd.atualiza_fornec(fornec)
    
    return redirect(url_for('consulta_agendamentos_fornec'))


@app.route('/sobre')
def sobre():
    print('run - sobre')
    return render_template('sobre.html')


@app.route('/sobre_fornec')
def sobre_fornec():
    print('run - _fornec')
    return render_template('sobre_fornec.html')


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
        retorno = homenail_bd.login_fornec(login)

        if retorno:
            session['usuario_logado'] = login.cpf
            return redirect(url_for('consulta_agendamentos_fornec'))
        else:
            return redirect(url_for('index'))

    elif login.cpf == 'admin' and login.senha == 'admin123':
            return redirect(url_for('exportar_dados'))

    else:
        return redirect(url_for('index'))

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    print('run - logout')

    session['usuario_logado'] = None
    # flash('Nenhum Usuário logado!')
    return redirect(url_for('index'))


@app.route('/exportar_dados')
def exportar_dados():
    print('run - exportar_dados')
    return render_template('exportar_dados.html')


@app.route('/exportar_dados_json')
def exportar_dados_json():
    print('run - exportar_dados_json')
    return redirect(url_for('exportar_dados'))


if __name__ == '__main__':
    app.run(debug=True) 
    