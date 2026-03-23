while True:
    try:
        num1 = int(input("Digite o primeiro valor\n> "))
        break
    except ValueError:
        print("Entrada Inválida!")

while True:
    try:
        num2 = int(input("Digite o segundo valor\n> "))
        break
    except ValueError:        
        print("Entrada Inválida!")

subtracao = num1 - num2

print ("A subtraçao é:\n>",subtracao)
