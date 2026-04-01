print("calculadora de multillicação")

while True:
    try:
        multiplicando = float(input('Digite um numero\n> '))
        break
    except ValueError:
         print('Entrada inválida!')

while True:         
    try:         
        multiplicador = float(input('Digite outro número:\n> '))
        break
    except ValueError:
        print('Entrada inválida!')
        
produto = multiplicando * multiplicador

print (f"O resultado é = {produto}")
