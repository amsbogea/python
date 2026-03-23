while True:
    try:
        nota1 = float(input('digite o valor da primeira nota.\n> '))
        if nota1 < 0 or nota1 > 10:
            print("Entrada inválida, digite valores entre 0 e 10.")
        else:
            break    
    except ValueError:
        print("Ops! Digite apenas números.")

while True:
    try:
        nota2 = float(input('digite o valor da segunda nota.\n> '))
        if nota2 < 0 or nota2 > 10:
            print("Entrada inválida, digite valores entre 0 e 10.")
        else:
            break
    except ValueError:
        print("Ops! Digite apenas números.")   

while True:
    try:
        nota3 = float(input('digite o valor da terceira nota.\n> '))
        if nota3 < 0 or nota3 > 10:
            print("Entrada inválida, digite valores entre 0 e 10.")
        else:
            break
    except ValueError:
        print("Ops! Digite apenas números.")

media = ((nota1 + nota2 + nota3) / 3)

print(f"\n\n> A media das notas do aluno é {media}.")

if media < 7:
    print('> Aluno reprovado')
else:
    print("> Aluno aprovado")