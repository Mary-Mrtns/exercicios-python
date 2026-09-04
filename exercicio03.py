# Exercício 3 - Validador de senha

# Peço a senha antes do laço pra já ter algo pra testar na primeira volta
senha = input("Digite uma senha: ")

# while que só para quando a senha atender os 3 critérios ao mesmo tempo
senha_valida = False
while not senha_valida:
    tem_tamanho = len(senha) >= 8 
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)

    if tem_tamanho and tem_numero and tem_maiuscula:
        senha_valida = True
    else:
        # Fui checando cada critério separado pra avisar exatamente o que falta
        if not tem_tamanho:
            print("Senha inválida, a senha precisa ter pelo menos 8 caracteres! ")
        if not tem_numero:
            print("Senha inválida, tem que conter pelo menos um número!")
        if not tem_maiuscula:
            print("Senha inválida, tem que conter pelo menos uma letra maiúscula!")
        senha = input("Digite a senha novamente seguindo os critérios: ")

print("Senha aceita!")