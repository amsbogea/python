# --- FUNÇÃO DE CÁLCULO DO INSS (Lógica Progressiva 2026) ---
def calcular_inss(valor_salario):
    faixas = [
        (1621.00, 0.075),
        (2902.84, 0.09),
        (4354.27, 0.12),
        (8475.55, 0.14)
    ]
    total_inss = 0
    limite_anterior = 0
    salario_para_calculo = min(valor_salario, 8475.55)

    for limite, aliquota in faixas:
        if salario_para_calculo > limite:
            total_inss += (limite - limite_anterior) * aliquota
            limite_anterior = limite
        else:
            total_inss += (salario_para_calculo - limite_anterior) * aliquota
            break
    return total_inss

# --- ENTRADA DE DADOS ---
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

# --- PROCESSAMENTO ---
# Agora chamamos a função para o cálculo correto
inss = calcular_inss(SalBruto)

desTicket = float(ticket * 0.15)

if transporte > 0:
    desTransporte = float(SalBruto * 0.06)
else:
    desTransporte = 0

descontos = inss + desTransporte + desTicket
SalLiquido = SalBruto - descontos

# --- SAÍDA ---
print(f"\n\n> O desconto do ticket é R$ {desTicket:.2f}")
print(f"> O desconto do transporte é R$ {desTransporte:.2f}")
print(f"> O desconto do INSS (Progressivo) é R$ {inss:.2f}")
print("-" * 30)
print(f"> O total de desconto é R$ {descontos:.2f}")
print(f"> O salario liquido é R$ {SalLiquido:.2f}")
