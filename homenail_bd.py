import psycopg2 as pg
from models import Cliente, Fornecedor, Agendamento


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

    def login_cliente(cpf, senha):
        print('HomeNail_login_cliente')
        sql = f"SELECT * FROM t_clientes WHERE cpf = '{cpf}' AND senha = '{senha}'"

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


    def cadastrar_fornecedor(nome, cpf, senha, telefone, cidade, estado):
        print(HomeNail_cadastrarFornecedor)
        sql = f"INSERT INTO t_fornecs (nome, cpf, senha, telefone, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cidade}', '{estado}')"

        cur = con.cursor()
        cur.execute(sql)


except Exception as erro:
    print(erro)
