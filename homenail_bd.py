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

        # for parametros in usuario:
        #     if parametros[2] == '{cpf}' and parametros[3] == '{senha}':
        #         return True
        #     else:
        #         return False

        if usuario:
            return True
        else:
            return False


    def cliente(nome, cpf, senha, telefone, cep, rua, numero, cidade, estado):

        print('teste cliente')

        sql = f"INSERT INTO t_clientes (nome, cpf, senha, telefone, cep, rua, numero, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cep}', '{rua}', '{numero}', '{cidade}', '{estado}') RETURNING id"

        print(nome, cpf, senha, telefone, cep, rua, numero, cidade, estado)

        cur = con.cursor()
        cur.execute(sql)
        id = cur.fetchone()[0]
        con.commit()

        print(id)
    
        if id:
            return True
        else:
            return False


    def cadastrarFornecedor(nome, cpf, senha, telefone, cidade, estado):
        sql = f"INSERT INTO t_fornecs (nome, cpf, senha, telefone, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cidade}', '{estado}')"

        print(nome, cpf, senha, telefone, cidade, estado)

        cur = con.cursor()
        cur.execute(sql)


  

except Exception as erro:
    print(erro)


# def imprimii():
#     return ('Deu certo seu boludo')

