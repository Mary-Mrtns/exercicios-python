# Exercício 10 - Caixa eletrônico simplificado

import random

saldo = 1000  # saldo inicial fixo, como pedido no exercício

# while True porque o menu tem que ficar repetindo até escolher sair
while True:
    print("\n--- Menu ---")
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")

    opcao = input("Escolha uma ação: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Digite aqui o valor do saque: "))

        # coloquei 10% de chance de "sem cédulas" antes de checar o saldo (desafio extra)
        if random.random() < 0.10:
            print("Operação não realizada: caixa sem cédula no momento.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "3":
        valor = float(input("Digite aqui o valor do depósito: "))
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "4":
        print("Saindo do programa. Obrigado por utilizar o caixa eletrônico!")
        break # break pra sair do while True

    else:
        print("Opção inválida. Tente novamente.")