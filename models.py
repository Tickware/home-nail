class Cliente:
    def __init__(self, nome, cpf, senha, telefone, cep, rua, numero, cidade, estado, id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.telefone = telefone
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado


class Fornec:
    def __init__(self, nome, cnpj, senha, telefone, cidade, estado, id=None):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.senha = senha
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado


class Agendamento:
    def __init__(self, cpf_cliente, cnpj_fornec, tp_servico, data, hora, id=None):
        self.id = id
        self.cpf_cliente = cpf_cliente
        self.cnpj_fornec = cnpj_fornec
        self.tp_servico = tp_servico
        self.data = data
        self.hora = hora

class Login:
    def __init__(self, cpf, senha):
        self.cpf = cpf
        self.senha = senha
