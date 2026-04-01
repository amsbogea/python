# Peça para o usuário digitar uma frase. O seu programa deve contar quantas vogais (a, e, i, o, u) existem nessa frase e exibir o total.

frase = 'Alex Miranda da Silva'#.lower().strip()
vogais = 'aeiouAEIOU'
contador = 0

for letras in frase:
    if letras in vogais:
        contador = contador + 1

print(contador)