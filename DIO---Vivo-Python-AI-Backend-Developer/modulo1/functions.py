SAQUE_MAXIMO = 500
N_SAQUES = 3
EXTRATO = ""
SALDO = 0
CONTAS = []
USUARIOS = []
AGENCIA = "0001"


def menu():
    print("\n" + "="*33)
    print("============= BANK ==============")
    print("="*33+ "\n")
    print("d. Depositar")
    print("s. Sacar")
    print("e. Extrato")
    print("nu. Criar usuário")
    print("cc. Criar conta")
    print("lc. Listar contas")
    print("q. Sair")
    print("\n" + "="*33)
    print("="*33 + "\n")
    


def saque():
    global SALDO, EXTRATO, N_SAQUES  # Declarar as variáveis globais
    saque = float(input("Digite o valor a sacar: "))
    if saque <= 0:
        print("Valor inválido. Tente novamente.")
    elif SALDO < saque:
        print(f"Você não pode sacar, pois seu saldo é menor que o valor desejado. Seu saldo é R$ {SALDO:.2f}")
    elif saque > SAQUE_MAXIMO:
        print(f"Você não pode sacar, pois o valor máximo para saque é R$ {SAQUE_MAXIMO:.2f}")
    elif N_SAQUES == 0:
        print("Você não pode mais sacar, pois já atingiu o número máximo de saques.")
    else:
        EXTRATO += f"Saque: R$ {saque:.2f}\n"
        SALDO -= saque
        N_SAQUES -= 1
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        print(f"Seu saldo atual é R$ {SALDO:.2f}")
    


def deposito():
    global SALDO, EXTRATO  # Declarar as variáveis globais
    deposito = float(input("Digite o valor a depositar: "))
    if deposito <= 0:
        print("Valor inválido. Tente novamente.")
    else:
        SALDO += deposito
        EXTRATO += f"Depósito: R$ {deposito:.2f}\n"
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
        print(f"Seu saldo atual é R$ {SALDO:.2f}")
    


def extrato():
    global SALDO, EXTRATO  # Declarar as variáveis globais
    if EXTRATO == "":
        print("Não foram realizadas movimentações.")
    else:
        print("\n============= EXTRATO ================")
        print(EXTRATO)
        print("======================================")
        print(f"\nSaldo: R$ {SALDO:.2f}")
        print("======================================")

def criar_usuario():
    global USUARIOS  # Declarar a variável global
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite a cpf do usuário: ")
    endereco = input("Digite o endereço do usuário, Estado - Cidade - Rua - Número: ")
    if filtrar_usuario(cpf):
        print("Usuário já cadastrado.")
        return
    if not nome or not cpf or not endereco:
        print("Nome, CPF e endereço são obrigatórios.")
    elif len(cpf) != 11:
        print("CPF inválido. O CPF deve conter 11 dígitos.")
    else:
        usuario = {"nome": nome, "cpf": cpf, "endereco": endereco}
        USUARIOS.append(usuario)
        print(f"Usuário {nome} criado com sucesso!")
    

def filtrar_usuario(cpf):
    global USUARIOS  # Declarar a variável global
    for usuario in USUARIOS:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta():
    global CONTAS  # Declarar a variável global
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if not usuario:
        print("Usuário não encontrado.")
        return

    # Verificar se o CPF já possui uma conta
    for conta in CONTAS:
        if conta["usuario"]["cpf"] == cpf:
            print("Este CPF já possui uma conta associada.")
            return

    numero_conta = len(CONTAS) + 1
    conta = {"usuario": usuario, "saldo": 0, "numero_conta": numero_conta, "agencia": AGENCIA}
    CONTAS.append(conta)
    print(f"Conta criada com sucesso para o usuário {usuario['nome']}!")
    
    
def listar_contas():
    global CONTAS  # Declarar a variável global
    if not CONTAS:
        print("Nenhuma conta cadastrada.")
        return
    for conta in CONTAS:
        print("\n" + "="*40)
        print(f"Conta: {conta['numero_conta']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print("="*40 + "\n")