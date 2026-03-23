while True:
    try:
        dividendo = int(input("Digite o dividendo.\n"))
        break
    except ValueError:
        print("Entrada inválida!")

while True:
        try:
            divisor = int(input("Digite do divisor.\n"))
            break
        except ValueError:
            print("Entrada inválida!")

resto = dividendo % divisor

print ("O resto da  divisao é:", resto)