menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou. O valor informado é inválido.")

    elif opcao == "s":
        print("Sacar")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Sem saldo suficiente")

        elif excedeu_limite:
            print("Limite de saque excedido")

        elif excedeu_saques:
            print("Número de saques excedidos")

        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou. O valor informado é inválido.")


    elif opcao == "e":
        print("Extrato")
        print("\n=============Extrato===================\n")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo : R$ {saldo:.2f}")
        print("\n=======================================")


    elif opcao == "q":
        break

    else:
        print("Operação inválida. Selecione novamente a operação desejada.")
