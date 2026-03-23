nota1 = float(input('digite o valor da primeira nota.\n> '))
nota2 = float(input('digite o valor da segunda nota.\n> '))
nota3 = float(input('digite o valor da terceira nota.\n> '))

media = ((nota1 + nota2 + nota3) / 3)

print(f"\n\n> A media das notas do aluno é {media}.")

if media < 7:
    print('> Aluno reprovado')
else:
    print("> Aluno aprovado")