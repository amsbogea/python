def adicao(a , b): return a + b
def subt(a , b): return a - b
def mult (a , b): return a * b
def div(a , b): return a / b if b != 0 else "Erro: Divisão por zero"
def div_int(a , b): return a // b if b != 0 else "Erro: Divisão por zero"
def resto_div(a , b): return a % b if b != 0 else "Erro: Divisão por zero"

while True:
    print('\n--- CALCULADORA ---')
    print('1. Somar | 2. Subtrair | 3. Multiplicar | 4. Dividir | 5. Divisão Inteira | 6. Resto da Divisão | 0. Sair')    

    # Solicitar a escolha do usuário    
    escolha = input('Escolha uma operação: ')

    if escolha == '0':
        print('Encerrando a calculadora. Até mais!')
        break

    if escolha in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))

                if escolha == '1':
                    resultado = adicao(num1, num2)
                    print(f'Resultado da soma de {num1} + {num2} = {resultado}')
                elif escolha == '2':
                    resultado = subt(num1, num2)
                    print(f'Resultado da subtração de {num1} - {num2} = {resultado}')
                elif escolha == '3':
                    resultado = mult(num1, num2)
                    print(f'Resultado da multiplicação de {num1} * {num2} = {resultado}')
                elif escolha == '4':
                    resultado = div(num1, num2)
                    print(f'Resultado da divisão de {num1} / {num2} = {resultado}')
                elif escolha == '5':
                    resultado = div_int(num1, num2)
                    print(f'Resultado inteiro da divisão de {num1} // {num2} = {resultado}')
                elif escolha == '6':
                    resultado = resto_div(num1, num2)
                    print(f'Resto da divisão de {num1} % {num2} = {resultado}')
            except ValueError:
                print('Erro: Por favor, digite um número válido.')
