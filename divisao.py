'''
Escreva um programa que solicite ao usuário dois números: o dividendo e o divisor. 
O programa deve realizar a divisão do dividendo pelo divisor e exibir o resultado. 
No entanto, o programa deve incluir validação de erro para garantir que o divisor não seja zero, evitando assim uma divisão por zero. 
Se o usuário tentar dividir por zero, o programa deve exibir uma mensagem de erro e solicitar que ele insira um divisor válido.
'''
# Função para ler um número real com validação de erro
def ler_numero(mensagem):
    """Lê um número real do usuário com validação de erro."""
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite um número.")

# --- Execução ---
dividendo = ler_numero("Digite o dividendo\n> ")

while True:
    divisor = ler_numero("Digite o divisor\n> ")
    if divisor != 0:
        break
    print("❌ O divisor não pode ser zero. Por favor, digite um número diferente de zero.")

# Realiza a divisão e calcula o resto
quociente = dividendo / divisor
resto = dividendo % divisor
divisao_inteira = dividendo // divisor

# Exibe os resultados
print(f"O quociente da divisão é: {quociente}")
print(f"O resto da divisão é: {resto}")
print(f"A divisão inteira é: {int(divisao_inteira)}")