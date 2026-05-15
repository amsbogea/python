'''
Escreva um programa que faça o seguinte:
Use um loop para pedir ao usuário 5 números inteiros quaisquer e armazene todos eles dentro de uma lista (dica: use lista.append(numero)).
Crie duas listas vazias adicionais: multiplos_de_3 e outros_numeros.
Use um loop for para percorrer a lista dos 5 números que o usuário digitou.
Dentro desse loop, verifique cada número:
Se o número for múltiplo de 3 (resto da divisão por 3 igual a 0), adicione-o na lista multiplos_de_3.
Se não for, adicione-o na lista outros_numeros.
No final do programa, fora de qualquer loop, imprima o conteúdo das duas listas prontas na tela.
'''

# Criando a lista para armazenar os números do usuário
numeros = []
multiplos_de_3 = []
outros_numeros = []

for i in range(5):
    while True:
        try:
            # Pedindo ao usuário para digitar 5 números inteiros
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

# Filtrando os números
for numero in numeros:
    if numero % 3 == 0:
        multiplos_de_3.append(numero)
    else:
        outros_numeros.append(numero)

# Imprimindo os resultados
print("Números múltiplos de 3:")
print(multiplos_de_3)
print("Outros números:")
print(outros_numeros)