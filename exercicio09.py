# Exercício 9 - Verificador de números primos

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

contador_primos = 0

# o for de fora percorre cada número do intervalo que foi escolhido
for numero in range(inicio, fim + 1):
    # números menores que 2 nunca são primos, então já corto aqui
    if numero < 2:
        print(f"{numero} -> não primo")
        continue

    eh_primo = True

    # em vez de testar até o número - 1, só testo até a raiz quadrada
    # (desafio extra, fica bem mais rápido pra números grandes)
    limite = int(numero ** 0.5)
    divisor = 2

    # while de dentro testa os divisores; se achar um, já sei que não é primo
    while divisor <= limite:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1

    if eh_primo:
        print(f"{numero} -> primo")
        contador_primos += 1
    else:
        print(f"{numero} -> não primo")

print(f"\nQuantidade de números primos encontrados: {contador_primos}")