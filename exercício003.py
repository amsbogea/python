#crie um programa que some dois numeros.

while True:
    try:
        numero1 = int(input('Digite o primeiro número: '))
        break
    except ValueError:
        print('Entrada inválida! Por favor digite um número inteiro! ')    
        
while True:
        try: 
            numero2 = int(input('Digite o segundo número: '))
            break
        except ValueError:
            print('Entrada inválida! Por favor digite um número: ')
            
soma = numero1 + numero2

print(f"A soma de {numero1} + {numero2} = {soma}")