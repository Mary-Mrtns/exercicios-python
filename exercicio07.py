# Exercício 7 - Calculadora de média escolar

n = int(input("Quantas notas você vai digitar?: "))

# coloquei esse while pra travar se a pessoa digitar 0 ou número negativo, senão dava erro de divisão
while n <= 0:
    print("Quantidade inválida! Digite um número maior que zero.")
    n = int(input("Quantas notas você vai digitar?: "))

soma = 0
maior = None
menor = None

# aqui utilizei o for para ler as n notas   
# (não podia usar lista, então guardei só em duas variáveis mesmo)
for i in range(1, n + 1):
    nota = float(input(f"Digite a nota {i}: "))
    soma += nota

    # na primeira nota maior/menor ainda são None, então essa nota já entra direto
    if maior is None or nota > maior:
        maior = nota
    if menor is None or nota < menor:
        menor = nota

media = soma / n

# classifiquei a média seguindo a regra do exercício
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"\nMédia: {media:.2f}")
print(f"Maior nota: {maior:.2f}")
print(f"Menor nota: {menor:.2f}")
print(f"Situação final: {situacao}")