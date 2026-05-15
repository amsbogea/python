'''
Escreva um programa que peça ao usuário um número inteiro positivo (faça a validação com try/except). 
O programa deve rodar um loop for de 1 até 20 e calcular a divisão inteira (//) do número digitado por cada etapa do loop.
'''

# Solicita ao usuário que digite um número inteiro positivo
while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Por favor, digite um número inteiro positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")

soma_total = 0

for  i in range(1, 21):
    resultado = numero // i
    soma_total += resultado
    print(f"{numero} // {i} = {resultado}")

    if soma_total > 50:
        print(f"Soma total é {soma_total} e atingiu ou ultrapassou 50. Parando o loop.")
        break   