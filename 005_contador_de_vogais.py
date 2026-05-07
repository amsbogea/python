# Peça para o usuário digitar uma frase. O seu programa deve contar quantas vogais (a, e, i, o, u) existem nessa frase e exibir o total.

from collections import Counter

frase = input('Digite um texto: ').lower()
vogais = 'aáàâãeéèêiíìîoóòôõuúùû'

# filtrar apenas as vogais e contar a frequência de cada uma
contagem = Counter(l for l in frase if l in vogais)

# exibir o relatório de vogais
for v in sorted(contagem.items()):
    print(f"Vogal '{v[0]}': {v[1]} vezes")

print(f"\nTotal de vogais: {sum(contagem.values())}")