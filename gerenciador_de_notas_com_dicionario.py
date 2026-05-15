'''
Desafio: O Gerenciador de Notas com Dicionário (dict)
Em Python, quando queremos associar informações (como o nome de uma pessoa e a nota dela), usamos Dicionários {}. Eles guardam informações no formato chave: valor.
Escreva um programa que faça o seguinte:
Crie um dicionário vazio chamado boletim = {}.
Use um loop for para pedir os dados de 3 alunos.
Dentro do loop, peça o nome do aluno (uma string) e a nota dele (um número float entre 0.0 e 10.0).
Faça a validação da nota com try/except. Se o usuário digitar algo inválido ou uma nota fora do intervalo (menor que 0 ou maior que 10), continue pedindo até ele acertar.
Adicione esses dados no dicionário usando o nome como chave: boletim[nome] = nota.
Após coletar os 3 alunos, use um loop para percorrer o dicionário e exibir a situação de cada um:
Se a nota for maior ou igual a 7.0, imprima: [Nome] aprovado com nota [Nota].
Se for menor, imprima: [Nome] reprovado com nota [Nota].
'''
boletim = {}

for i in range(3):

    # Validação do nome do aluno        
    while True:
        nome = input(f"Digite o nome do {i+1}º aluno: ").strip().title() # Remove espaços e coloca a primeira letra em maiúscula
        # Verifica se o nome contem apenas letras e o campo não está vazio
        if nome.replace(" ", "").isalpha() and "  " not in nome and nome != "":
            break
        else:
            print("Por favor, digite um nome válido (apenas letras e espaços simples).")

    # Validação da nota do aluno
    while True:
        try:
            nota = float(input(f"Digite a nota de {nome}: "))
            if 0 <= nota <= 10:
                boletim[nome] = nota
                break
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Por favor, digite um número válido.")

# Exibe a situação de cada aluno
for nome, nota in boletim.items():
    if nota >= 7.0:
        print(f"{nome} aprovado com nota {nota:.1f}.")
    else:
        print(f"{nome} reprovado com nota {nota:.1f}.")