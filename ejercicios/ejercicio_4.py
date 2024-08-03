"""
Franco Salvador Talarico - 4°3

Requerir al usuario que ingrese un número entero e informar si es primo o no,
utilizando una función booleana que lo decida.
"""

from funciones.esPrimo import esPrimo

numero = int(1)

while(numero != 0):
    numero = int(input("Ingrese un número: "))

    if(esPrimo(numero)):
        print(f'El número {numero} es primo.')
    else:
        print(f'El número {numero} NO es primo.')