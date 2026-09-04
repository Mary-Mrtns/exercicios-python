# Exercício 4 - Jogo de adivinhação

import random

# Sorteio do número que o jogador vai ter que adivinhar
numero_sorteado = random.randint(1, 100)

tentativas = 0
acertou = False
max_tentativas = 10  # limitei a 10 tentativas (desafio extra)

# while roda até o jogador acertar ou estourar o limite de tentativas
while tentativas < max_tentativas and not acertou:
    chute = int(input("Tente adivinhar o número sorteado entre 1 a 100: "))
    tentativas += 1

    if chute == numero_sorteado:
        acertou = True
    elif chute > numero_sorteado:
        print("O número sorteado é menor que o seu palpite.")
    else:
        print("O número sorteado é maior que o seu palpite.")

if acertou:
    print(f"Parabéns! Você acertou em {tentativas} tentativas(s).")
else:
    # se acabou as tentativas eu mostro qual era o número (desafio extra)
    print(f"Você não acertou dentro do limite de {max_tentativas} tentativas.")
    print(f"O número sorteado era: {numero_sorteado}")