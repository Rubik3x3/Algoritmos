"""
Franco Salvador Talarico - 4°3

Escribir un programa que pida números positivos al usuario. 
Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. 
Utilizar una o más funciones, según sea necesario.
"""

from funciones.sumaDigitos import sumaDigitos

numero = int(1)
contador = 0

mayor = int(0)
menores_de_10 = int(0)

while(numero != 0):
    numero = int(input("Ingrese un número: "))
    numDigitos = sumaDigitos(numero)
    if(contador == 0):
        mayor = numDigitos
    else:
        if(numDigitos > mayor):
            mayor = numDigitos
    if numDigitos < 10:
        menores_de_10 += 1
    contador += 1

print(f'Mayor: {mayor}\nMenores de 10: {menores_de_10}')
