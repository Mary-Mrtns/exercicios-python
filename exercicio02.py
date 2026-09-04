# Exercício 2 - Tabuada interativa

#começo com a variável n para que a pessoa escolha o número que ela quer que seja feita a tabuada
n = int(input("Digite um número inteiro n: "))

#início e fim, aqui a pessoa pode escolher da onde a tabuada vai querer iniciar e terminar (desafio extra)
inicio = int(input("Digite um número de inicio da tabuada: "))
fim = int(input("Digite um número de fim da tabuada: "))

#parte lógica, os números serão multiplicados e depois imprimidos na tela de acordo com o que foi escolhido
for i in range(inicio, fim + 1):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")