def menu():
    print("\n" + "="*33)
    print("============= BANK ==============")
    print("="*33+ "\n")
    print("d. Depositar")
    print("s. Sacar")
    print("e. Extrato")
    print("q. Encerrar atendimento")
    print("\n" + "="*33)
    print("="*33 + "\n")
    
    
n_saques = 3
saldo = 0
saque_maximo = 500
extrato = ""

while True:
    menu()
    opcao = input("Escolha uma opção: ").strip().lower()
    if opcao == "d":
        deposito = float(input("Digite o valor a depositar: "))
        if deposito <= 0:
            print("Valor inválido. Tente novamente.")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
            print(f"Seu saldo atual é R$ {saldo:.2f}")
            
    elif opcao == "s":
        saque = float(input("Digite o valor a sacar: "))
        if saque <= 0:
            print("Valor inválido. Tente novamente.")
        elif saldo < saque:
            print(f"Você não pode sacar, pois seu saldo é menor que o valor desejado.")
            print(f"Seu saldo atual é R$ {saldo:.2f}")
        elif saque > saque_maximo:
            print(f"Você não pode sacar, pois o valor máximo para saque é R$ {saque_maximo:.2f}")
        elif n_saques== 0:
            print("Você não pode mais sacar, pois já atingiu o número máximo de saques.")
        else:
            extrato += f"Saque: R$ {saque:.2f}\n"
            saldo -= saque
            n_saques-= 1
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
    elif opcao == "e":
            print("\n============= EXTRATO ================")
            print(extrato if extrato else "Não foram realizadas movimentações.")
            print("======================================")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("======================================")
    
    elif opcao == "q":
        print("Encerrando atendimento...")
        print("Obrigado por utilizar nossos serviços!")
        break
    else:
        print("Opção inválida. Tente novamente.")