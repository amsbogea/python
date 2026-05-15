'''
    Escreva um programa em Python que peça para o usuário digitar um número inteiro positivo inicial. 
    O programa deve, então, gerar uma sequência automática com os próximos 10 números consecutivos a partir dele.
'''

# Solicita ao usuário que digite um número inteiro positivo
while True:
    try:
        numero_inicial = int(input("Digite um número inteiro positivo: "))
        if numero_inicial < 0:
            print("Por favor, digite um número inteiro positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")

# Gera e exibe a sequência de 10 números consecutivos
print("Sequência de números consecutivos:")
for i in range(10):
    numero_final = numero_inicial + i
    calculo = numero_final // numero_inicial
    if calculo % 2 != 0:
        print(f"{numero_final} // {numero_inicial} = {calculo}")
