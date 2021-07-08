SalBruto = input("Digite o salario bruto: ")

transporte = input("Digite o valor do transporte: ")

ticket = input("Digite o valor do ticket: ")

inss = (float(SalBruto * 9)/100)

desTicket = (float(ticket*15)/100)

desTransporte = (float(transporte*6)/100)

descontos = (float (inss + desTransporte + desTicket))

SalLiquido = (float (SalBruto - descontos))

print ("O desconto do ticket é R$", desTicket)

print ("O desconto do transporte é R$", desTransporte)

print ("O total de desconto é R$", descontos)

print ("O salario liquido é R$", SalLiquido)
