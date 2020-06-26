import psycopg2 as pg

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

    def login(cpf, senha):
        sql = f"SELECT * FROM t_clientes WHERE cpf = '{cpf}' AND senha = '{senha}'"

        print(cpf)

        cur = con.cursor()
        cur.execute(sql)
        usuario = cur.fetchone()

        if usuario:
            return True
        else:
            return False


    def cliente(nome, cpf, senha, telefone, cep, rua, numero, cidade, estado):

        sql = f"INSERT INTO t_clientes (nome, cpf, senha, telefone, cep, rua, numero, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cep}', '{rua}', '{numero}', '{cidade}', '{estado}') RETURNING id"

        cur = con.cursor()
        cur.execute(sql)
        id = cur.fetchone()[0]
        con.commit()

        if id:
            return True
        else:
            return False


    def cadastrarFornecedor(nome, cpf, senha, telefone, cidade, estado):
        sql = f"INSERT INTO t_fornecs (nome, cpf, senha, telefone, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cidade}', '{estado}')"

        cur = con.cursor()
        cur.execute(sql)


except Exception as erro:
    print(erro)
