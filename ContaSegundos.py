# valida a entrada do usuário para garantir que seja um número inteiro
while True:
    try:
        total_segs = int(input("Digite o numero de segundos que deseja converter: "))
        break
    except ValueError:
        print("Entrada Inválida!\n")

# processa a conversão de segundos para horas, minutos e segundos
horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

# exibe o resultado da conversão no terminal
print(f"{total_segs} segundos equivalem a {horas} hora(s), {minutos} minuto(s) e {segs_restantes_final} segundo(s).")
