def par_impar(a):
    if a % 2 == 0:
        return ("este numero é par")
    else:
        return ("este numero é impar")
        
valor_digitado = int(input("digite um numero: "))            
print(par_impar(valor_digitado))