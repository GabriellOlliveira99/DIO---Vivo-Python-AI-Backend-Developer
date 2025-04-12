from functions import deposito, saque, extrato, menu, listar_contas, criar_usuario, criar_conta

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()
        if opcao == "d":
            deposito()
        elif opcao == "s":
            saque()
        elif opcao == "e":
            extrato()
        elif opcao == "nu":
            criar_usuario()
        elif opcao == "cc":
            criar_conta()
        elif opcao == "lc":
            listar_contas()
        elif opcao == "q":
            print("Sair")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
    
