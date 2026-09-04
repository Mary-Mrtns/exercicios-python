# Exercício 1 - Classificador de IMC

# Peguei peso e altura do usuário pra calcular o IMC com a fórmula dada
peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))

IMC = peso / (altura ** 2)

# Usei if/elif/else pra comparar o IMC com os intervalos da tabela do exercício
if IMC < 18.5:
    classificação = "Abaixo do peso"
elif IMC < 25.0:
    classificação = "Peso normal"
elif IMC < 30.0:
    classificação = "Sobrepeso"
else:
    classificação = "Obesidade"

# Formatei com 2 casas decimais pra ficar mais fácil de ler (desafio extra)
print(f"Seu IMC é: {IMC:.2f}")
print(f"Sua classificação é: {classificação}")