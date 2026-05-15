while True:
    try:
        a = int(input("Digite o primeiro valor\n> "))
        break
    except ValueError:
        print("Entrada inválida!")
while True:
    try:
        b = int(input("Digite o segundo valor\n> "))
        break
    except ValueError:
        print("Entrada inválida!")
soma = a + b

print (f"A soma de {a} + {b} = {soma}")