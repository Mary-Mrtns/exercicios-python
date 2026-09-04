# Exercício 8 - Cara ou coroa

import random

vitorias = 0
derrotas = 0
continuar = "sim"

# while que repete enquanto o jogador quiser continuar jogando
while continuar == "sim":
    aposta = input("Aposte 'cara' ou 'coroa': ").strip().lower()
    resultado = random.choice(["cara", "coroa"])

    print(f"Resultado sorteado: {resultado}")

    if aposta == resultado:
        print("Você acertou!") 
        vitorias += 1
    else:
        print("Você errou!")
        derrotas += 1

    continuar = input("Deseja jogar novamente? (sim/não): ").strip().lower()

total_jogadas = vitorias + derrotas

# no final calculei o percentual de acerto em cima do total de jogadas
print("\n--- Resultado final ---")
print(f"Vitórias: {vitorias}")
print(f"Derrotas: {derrotas}")

if total_jogadas > 0:
    percentual = (vitorias / total_jogadas) * 100
    print(f"Percentual de acerto: {percentual:.2f}%")
else:
    print("Nenhuma rodada foi jogada")