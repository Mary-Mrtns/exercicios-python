# Exercício 6 - Sorteio de bingo simplificado

import random

# em vez de fixar 5 números, deixei o jogador escolher quantos quer sortear (desafio extra)
quantidade = int(input("Quantos números deseja sortear?: "))

# não podia usar lista, então fui somando em variáveis contadoras mesmo
contador_pares = 0
contador_multiplos_5 = 0

# for sorteando um número por vez e já contando na hora
for i in range(quantidade):
    numero = random.randint(1, 60)
    print(f"Número sorteado: {numero}")

    if numero % 2 == 0:
        contador_pares += 1
    if numero % 5 == 0:
        contador_multiplos_5 += 1 

print("\n--- Resumo do sorteio ---")
print(f"Quantidade de números pares: {contador_pares}")
print(f"Quantidade de números múltiplos de 5: {contador_multiplos_5}")