def menu():
    print("\n" + "="*33)
    print("============= BANK ==============")
    print("="*33+ "\n")
    print("d. Depositar")
    print("s. Sacar")
    print("e. Extrato")
    print("q. Sair")
    print("\n" + "="*33)
    print("="*33 + "\n")
    
    
N_SAQUES = 3
SALDO = 0
SAQUE_MAXIMO = 500
EXTRATO = ""

while True:
    menu()
    opcao = input("Escolha uma opção: ").lower()
    if opcao == "d":
        deposito = float(input("Digite o valor a depositar: "))
        if deposito <= 0:
            print("Valor inválido. Tente novamente.")
        else:
            SALDO += deposito
            EXTRATO += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
            print(f"Seu saldo atual é R$ {SALDO:.2f}")
            
    elif opcao == "s":
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
    elif opcao == "e":
        if EXTRATO == "":
            print("Não foram realizadas movimentações.")
        else:
            print("\n============= EXTRATO ================")
            print(EXTRATO)
            print("======================================")
            print(f"\nSaldo: R$ {SALDO:.2f}")
            print("======================================")
        
    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Opção inválida. Tente novamente.")