def showMenu():
    print(
          f"Digite a opção que deseja:\n"
          f"1 - Sacar \n"
          f"2 - Depositar\n"
          f"3 - Ver saldo\n"
          f"0 - Sair do menu")


def sacar(saldo, qtd):
    saldo -= qtd
    return saldo

def depositar(saldo, qtd):
    return saldo + qtd

def showSaldo(saldo):
    print(f"Seu saldo é R$ {saldo}")


def iniciar():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}")
    showMenu()
    opt = int(input())
    saldo = 0.0
    qtd_de_saque = 0


    while(opt != 0):
        if(opt == 1):
            if(qtd_de_saque >= 3):
                print("Quantidade limite de saques atingida")
            else:
                qtd = float(input("Digite o valor do saque: "))
                if(saldo < qtd):
                    print("Saldo insuficiente")
                elif(qtd > 500):
                    print("Limite de valor de saque atingido")
                else:
                    qtd_de_saque += 1
                    saldo = sacar(saldo, qtd)
        elif(opt == 2):
            qtd = float(input("Digite o valor do deposito: "))
            saldo = depositar(saldo, qtd)
        elif(opt == 3):
            showSaldo(saldo)
        else:
            print("Opção inválida")
        showMenu()
        opt = int(input())


iniciar()