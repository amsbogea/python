while True:
    try:    
        celcius = float(input('digite a temperatura em celcius:\n > '))
        break
    except ValueError:
        print("Entrada inválida!")

farenheit = (celcius * 1.8 + 32)
print(f"{celcius} graus Celcius é equivalente a {farenheit} graus Farenheit!")