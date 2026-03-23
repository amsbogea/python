while True:
    try:
        TemperaturaFahrenheit = float(input("Digite uma temperatura em Fahrenheit: "))
        break
    except ValueError:
        print("Entrada inválida")

TeperaturaCelsius = ( float(TemperaturaFahrenheit) - 32) *5 /9

print ("A temperatura em celsius é ", TeperaturaCelsius)
