import psycopg2 as pg
from models import Cliente, Fornecedor, Agendamento, Login


try:
    con = pg.connect(
        database = 'db_homeNailTeste',
        user = 'postgres',
        password = 'postgres',
        host = '127.0.0.1',
        port = '5432'
    )

    ###Conectar no banco
    print('\n*** Banco conectado! Somente pessoal autorizado! ***\n')

    def login_cliente(login):
        print('HomeNail_login_cliente')
        sql = f"SELECT * FROM t_clientes WHERE cpf = '{int(login.cpf)}' AND senha = '{login.senha}'"

        cur = con.cursor()
        cur.execute(sql)
        usuario = cur.fetchone()

        if usuario:
            return True
        else:
            return False


    # def cadastrar_cliente(nome, cpf, senha, telefone, cep, rua, numero, cidade, estado): 
    def cadastrar_cliente(cliente): 
        print('HomeNail_Cadastro_Cliente')

        sql = f"INSERT INTO t_clientes (nome, cpf, senha, telefone, cep, rua, numero, cidade, estado) values('{cliente.nome}', {cliente.cpf}, '{cliente.senha}', {cliente.telefone}, '{cliente.cep}', '{cliente.rua}', {cliente.numero}, '{cliente.cidade}', '{cliente.estado}') RETURNING id"

        
        cur = con.cursor()
        cur.execute(sql)
        id = cur.fetchone()[0]
        con.commit()

        if id:
            return True
        else:
            return False

    def busca_dados_cliente(usuario_logado_cpf):
        print('HomeNail_editar_cliente')

        sql = f"SELECT * FROM t_clientes WHERE cpf = '{int(usuario_logado_cpf)}'"

        cur = con.cursor()
        cur.execute(sql)

        cliente = cur.fetchone()

        return cliente


    def atualiza_cliente(cliente):
        print('HomeNail_atualiza_cliente')

        sql = f"UPDATE t_clientes SET nome = '{cliente.nome}', senha = '{cliente.senha}', telefone =  {cliente.telefone}, cep = '{cliente.cep}', rua =  '{cliente.rua}', numero =  {cliente.numero}, cidade = '{cliente.cidade}', estado =  '{cliente.estado}'  WHERE cpf = {cliente.cpf}"
        cur = con.cursor()
        cur.execute(sql)
        con.commit()

    def cadastrar_fornecedor(nome, cpf, senha, telefone, cidade, estado):
        print('HomeNail_cadastrarFornecedor')
        sql = f"INSERT INTO t_fornecs (nome, cpf, senha, telefone, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cidade}', '{estado}')"

        cur = con.cursor()
        cur.execute(sql)
        con.commit()


except Exception as erro:
    print(erro)
