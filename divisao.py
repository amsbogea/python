while True:
    try:
        dividendo = float(input("Digite o dividendo\n> "))
        break
    except ValueError:
        print("Entrada inválida!")

while True:
    try:
        divisor = float(input("Digite o divisor\n> "))
        break
    except ValueError:
        print("Entrada inválida!")

quociente = dividendo / divisor
resto = dividendo % divisor

print ("O quociente da divisao é:", quociente)
print ("O resto da divisao é:", resto)
