# Crie um programa que solicite o nome do usuario e lhe mostre  uma mensagem de boas vindas.

while True:
    nome = input('Digite seu nome: ').strip()
        
    # Verifica se o campo não está vazio
    if not nome:
        print("O nome naão pode estar vazio")
        continue

# Verifica se há apenas letras e espaços simples
# (Não permite dois espaços seguidos "  " e garante que tudo seja letra/espaço)
    if nome.replace(" ", "").isalpha() and "  " not in nome:
        nome = nome.title() # transforma as primeiras letras em MAIUSCULAS e as demais minusculas (ex: Alex Miranda)
        break
    else:
        print("Operação inválida! Digite apenas letras com espaços simples entre os nomes.")    

print(f"Seja bem vindo, {nome}!")