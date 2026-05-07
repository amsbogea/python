while True:
    try:
        temperatura_fahrenheit = float(input("Digite uma temperatura em Fahrenheit: "))
        break
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números.")

temperatura_celsius = (temperatura_fahrenheit - 32) * 5 / 9

print(f"A temperatura em celsius é {temperatura_celsius:.2f}°C")