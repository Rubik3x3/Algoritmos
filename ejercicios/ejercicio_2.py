"""
Solicitar números al usuario hasta que ingrese el cero. 
Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).
"""

from funciones.sumaDigitos import sumaDigitos

numero = int(1)

while(numero != 0):
    numero = int(input("Ingrese un número: "))
    print(f'Suma de sus dígitos: {sumaDigitos(numero)}')
