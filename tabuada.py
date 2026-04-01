# Peça um número ao usuário e, usando um loop for, imprima a tabuada desse número de 1 a 10.

while True:
    try:
        numero = int(input('Digite um número\n> '))
        break
    except ValueError:
        print('Entrada inválida!')

print('\n')
for i in range(11):
    tabuada = numero + i
    print(f"{numero} + {i} = {tabuada}")

print('\n')        
i = 0

for i in range(11):
    tabuada = numero - i
    print(f"{numero} - {i} = {tabuada}")
    
print('\n')        
i = 0

for i in range(11):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")
    
print('\n')        
i = 0

for i in range(1, 11):
    tabuada = numero // i
    print(f"{numero} / {i} = {tabuada}")