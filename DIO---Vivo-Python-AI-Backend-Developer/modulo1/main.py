from functions import depositar, sacar, mostrar_extrato, criar_usuario, criar_conta, listar_contas, menu

def main():
    saque_maximo = 500
    n_saques = 3
    extrato = ""
    saldo = 0
    contas = []
    usuarios = []
    agencia = "0001"
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, n_saques = sacar(saldo, extrato, n_saques, saque_maximo)
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)
        elif opcao == "nu":
            usuarios = criar_usuario(usuarios)
        elif opcao == "cc":
            contas = criar_conta(contas, usuarios, agencia)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Sair")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
    
