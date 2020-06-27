import psycopg2 as pg
import os
os.system('cls')

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

    def menu():
        return '''*** HomeNail!! ***
    1 - Criar Tabela Clientes
    2 - Criar Tabela fornecedores
    3 - Criar Tabela Agenda
    4 - Cadastrar cliente
    5 - Cadastrar Fornecedor
    6 - Realizar Agendamento
    0 - Exit\n'''

    # ###Criar tabela t_clientes
    def criaTabelaClientes():
        os.system('cls')
        
        sql = 'CREATE TABLE t_clientes(id serial, nome varchar(100), cpf bigint, senha	varchar(50), telefone integer, cep varchar(9), rua varchar(50), numero integer, cidade varchar(50), estado varchar(2), UNIQUE(id), UNIQUE(cpf), CONSTRAINT pk_t_clientes PRIMARY KEY (id));'

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        print('Boa! Tabela Clientes criada!\n')

    # ###Criar tabela t_clientes
    def criaTabelaFornecs():
        os.system('cls')
    
        sql = 'CREATE TABLE t_fornecs(id serial, nome varchar(50), cpf bigint, senha varchar(50), telefone integer, cidade varchar(50), estado varchar(2), UNIQUE(id), UNIQUE(cpf), CONSTRAINT id_pk_t_fornecs PRIMARY KEY (id));'

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        print('Boa! Tabela Fornecedores criada!\n')

    # ###Criar tabela t_agenda
    def criaTabelaAgenda():
        os.system('cls')
        sql = 'CREATE TABLE t_agenda(id serial, id_cliente integer, id_fornec integer, tp_serviço varchar(1), status varchar(1), data date, hora time, UNIQUE(id), CONSTRAINT pk_t_agenda PRIMARY KEY (id), CONSTRAINT fk_t_agenda_clientes FOREIGN KEY (id_cliente) REFERENCES t_clientes(id), CONSTRAINT fk_t_agenda_fornecs FOREIGN KEY (id_fornec) REFERENCES t_fornecs(id));'

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        print('Boa! Tabela Agenda criada!\n')

    ###Insert
    # sql = "INSERT INTO tb_editora (nome) values('Edit5')"

    # cur = con.cursor()
    # cur.execute(sql)
    # con.commit()

    #Insert cliente
    def cadastraCliente():
        os.system('cls')
    
        nome = input('Informe o nome: ')
        cpf = input('CPF: ')
        senha = input('Senha: ')
        telefone = input('Telefone: ')
        cep = input('CEP: ')
        rua = input('Logradouro: ')
        numero = input('Número: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')        

        sql = f"INSERT INTO t_clientes (nome, cpf, senha, telefone, cep, rua, numero, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cep}', '{rua}', '{numero}', '{cidade}', '{estado}')"

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        print('Ae! Cliente inserido na base!\n')

    #Insert Fornecedor
    def cadastraFornec():
        os.system('cls')
        
        nome = input('Informe o nome: ')
        cpf = input('CPF: ')
        senha = input('Senha: ')
        telefone = input('Telefone: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')

        nome, cpf, senha, telefone, cidade, estado

        sql = f"INSERT INTO t_fornecs (nome, cpf, senha, telefone, cidade, estado) values('{nome}', '{cpf}', '{senha}', '{telefone}', '{cidade}', '{estado}')"

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        print('Ae! Fornecedor inserido na base!\n')

    ###Insert retornando ID
    # sql = "INSERT INTO tb_editora (nome) values('Edit9') RETURNING id"

    # cur = con.cursor()
    # cur.execute(sql)
    # id = cur.fetchone()[0]
    # print(f'Id inserido: {id}')
    # con.commit()

    # print('Ae! Dados inseridos na tabela!\n')

    # ###Insert retornando ID com FK
    # sql = "INSERT INTO tb_editora (nome) values('Edit10') RETURNING id"

    # cur = con.cursor()
    # cur.execute(sql)
    # id = cur.fetchone()[0]
    # print(f'Id inserido: {id}')
    # con.commit()


    # sql = f"INSERT INTO tb_livros (id_editora, nome) values({id}, 'Livro 1')"

    # cur = con.cursor()
    # cur.execute(sql)
    # con.commit()

    # print('Ae! Dados inseridos na tabela!\n')

    ###Select
    # sql = 'SELECT * FROM tb_editora ORDER BY id'
    # cur = con.cursor()
    # cur.execute(sql)

    # linhas = cur.fetchall()

    # for linha in linhas:
    #     print(f'ID = {linha[0]}\tNome = {linha[1]}')
    #     #print(f'Nome = {linha[1]}')

    # sql = 'SELECT * FROM tb_livros ORDER BY id'
    # cur = con.cursor()
    # cur.execute(sql)

    # linhas = cur.fetchall()

    # for linha in linhas:
    #     print(f'Id_editora = {linha[0]}\tId_livro = {linha[1]}\tNome livro = {linha[2]}')

    # con.close()

    while True:
        n = int(input(menu()))
    
        if n == 1:
            criaTabelaClientes()
    
        elif n == 2:
            criaTabelaFornecs()

        elif n == 3:
            criaTabelaAgenda()

        elif n == 4:
            cadastraCliente()

        elif n == 5:
            cadastraFornec()

        #elif n == 6:
            #geraAgenda()

        elif n == 0:
            print('Sessão Encerrada')
            break
        else:
            print('Opção Inválida, Tião!')

except Exception as erro:
    print(erro)

