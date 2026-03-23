while True:
    try:
        dividendo = int(input("Digite o dividendo.\n"))
        break
    except ValueError:
        print("Entrada Inválida!")

while True:
        try:
            divisor = int(input("Digite do divisor.\n"))
            break
        except ValueError:
            print("Entrada Iinválida!")

divisao = dividendo // divisor

print ("O quociente da  divisao é:", divisao)
