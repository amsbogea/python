# Peça para o usuário digitar uma frase. O seu programa deve contar quantas vogais (a, e, i, o, u) existem nessa frase e exibir o total.

frase = input('Digite um texto: ').lower().strip()
vogais = 'aeiou'
contador = 0

for letra in frase:
    if letra in vogais:
        contador = contador + 1

print('Este texto contem ',contador, ' vogal(is)')