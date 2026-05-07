# Exercício 003: Crie um programa que leia dois números e mostre a soma entre eles.
# Função para ler um número inteiro com tratamento de exceção
def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print('Entrada inválida! Por favor digite um número ou inteiro! ')

# uso da função para ler os números
numero1 = ler_numero('Digite o primeiro número: ')
numero2 = ler_numero('Digite o segundo número: ')
soma = numero1 + numero2
print(f"A soma de {numero1} + {numero2} = {soma}")