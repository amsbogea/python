#Entrada de dados do usuario
while True:
    try:
        SalBruto = float(input("Digite o salario bruto:\n>  "))
        break
    except ValueError:
        print("Entrada Inválida!") 
           
while True:
    try:
        transporte = float(input("Digite o valor do transporte: "))
        break
    except ValueError:
        print("Entrada Inválida!")
while True:
    try:
        ticket = float(input("Digite o valor do ticket: "))
        break
    except ValueError:
        print("Entrada inválida!")

#processamento
inss = (float(SalBruto * 9)/100)

desTicket = (float(ticket*15)/100)

desTransporte = (float(SalBruto*6)/100)

descontos = (float (inss + desTransporte + desTicket))

SalLiquido = (float (SalBruto - descontos))

#saida na tela do terminal
print ("\n\n> O desconto do ticket é R$", desTicket)

print ("\n> O desconto do transporte é R$", desTransporte)

print ("\n> O desconto do inss é R$", inss)

print ("\n> O total de desconto é R$", descontos)

print ("\n> O salario liquido é R$", SalLiquido)
