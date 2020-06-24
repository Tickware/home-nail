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
        sql = f"SELECT * FROM t_clientes WHERE cpf = '{cpf}'"

        cur = con.cursor()
        cur.execute(sql)
        usuario = cur.fetchall()

        for parametros in usuario:
            if parametros[2] == '{cpf}' and parametros[3] == '{senha}':
                return True
            else:
                return False

    # def cadastraCliente():
    #     os.system('cls')
    
    #     nome = input('Informe o nome: ')
    #     cpf = input('CPF: ')
    #     senha = input('Senha: ')
    #     telefone = input('Telefone: ')
    #     cep = input('CEP: ')
    #     rua = input('Logradouro: ')
    #     numero = input('Número: ')
    #     cidade = input('Cidade: ')
    #     estado = input('Estado: ')        

    #     sql = f"INSERT INTO t_clientes (nome, cpf, senha, telefone, cep, rua, numero, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cep}', '{rua}', '{numero}', '{cidade}', '{estado}')"

    #     cur = con.cursor()
    #     cur.execute(sql)
    #     con.commit()

    #     print('Ae! Cliente inserido na base!\n')    

except Exception as erro:
    print(erro)


# def imprimii():
#     return ('Deu certo seu boludo')

