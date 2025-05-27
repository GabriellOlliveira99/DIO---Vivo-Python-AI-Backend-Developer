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
    


def sacar(saldo, extrato, n_saques, saque_maximo): 
    saque = float(input("Digite o valor a sacar: "))
    if saque <= 0:
        print("Valor inválido. Tente novamente.")
    elif saldo < saque:
        print(f"Você não pode sacar, pois seu saldo é menor que o valor desejado. Seu saldo é R$ {saldo:.2f}")
    elif saque > saque_maximo:
        print(f"Você não pode sacar, pois o valor máximo para saque é R$ {saque_maximo:.2f}")
    elif n_saques == 0:
        print("Você não pode mais sacar, pois já atingiu o número máximo de saques.")
    else:
        extrato += f"Saque: R$ {saque:.2f}\n"
        saldo -= saque
        n_saques -= 1
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        print(f"Seu saldo atual é R$ {saldo:.2f}")
    
    return saldo, extrato, n_saques  # Retornar os valores atualizados
    


def depositar(saldo, extrato):
    deposito = float(input("Digite o valor a depositar: "))
    if deposito <= 0:
        print("Valor inválido. Tente novamente.")
    else:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
        print(f"Seu saldo atual é R$ {saldo:.2f}")
    
    return saldo, extrato  # Retornar os valores atualizados
    


def mostrar_extrato(saldo, extrato):
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print("\n============= EXTRATO ================")
        print(extrato)
        print("======================================")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite a cpf do usuário: ")
    endereco = input("Digite o endereço do usuário, Estado - Cidade - Rua - Número: ")

    if filtrar_usuario(cpf, usuarios):
        print("Usuário já cadastrado.")
        return usuarios

    if not nome or not cpf or not endereco:
        print("Nome, CPF e endereço são obrigatórios.")
        return usuarios

    elif len(cpf) != 11:
        print("CPF inválido. O CPF deve conter 11 dígitos.")
        return usuarios

    usuario = {"nome": nome, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")

    return usuarios  # Retornar a lista de usuários atualizada
    

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(contas, usuarios, agencia):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado.")
        return contas

    # Verificar se o CPF já possui uma conta
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            print("Este CPF já possui uma conta associada.")
            return contas

    numero_conta = len(contas) + 1
    conta = {"usuario": usuario, "saldo": 0, "numero_conta": numero_conta, "agencia": agencia}
    contas.append(conta)
    print(f"Conta criada com sucesso para o usuário {usuario['nome']}!")
    
    return contas  # Retornar a lista de contas atualizada
    
    
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print("\n" + "="*40)
        print(f"Conta: {conta['numero_conta']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print("="*40 + "\n")