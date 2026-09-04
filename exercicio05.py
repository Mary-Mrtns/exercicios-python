# Exercício 5 - Simulador de dados (par ou ímpar)

import random

Jogador = input("Digite seu nome: ")

jogar_novamente = "sim"

# contadores fora do while pra somar mesmo se o jogador jogar mais de uma "leva" de rodadas
total_pares = 0 
total_impares = 0

# esse while de fora é o (desafio extra): pergunta se o jogador quer jogar de novo
while jogar_novamente == "sim":
    n = int(input(f"Quantas rodadas você quer jogar {Jogador}: "))

# for rodando as n rodadas que foi pedida
    for rodada in range(1, n + 1):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1, 6)
        soma = dado1 + dado2

        if soma % 2 == 0:
            print(f"Rodada {rodada}: {dado1} + {dado2} = {soma} (PAR)")
            total_pares += 1
        else:
            print(f"Rodada {rodada}: {dado1} + {dado2} = {soma} (IMPAR)")
            total_impares += 1

    jogar_novamente = input("Deseja jogar novamente (sim/não): ").strip().lower()

# resumo geral de tudo que foi jogado, mesmo que tenha jogado mais de uma vez
print(f"Quantidade de resultados pares: {total_pares}") 
print(f"Quantidade de resultados impares: {total_impares}") 