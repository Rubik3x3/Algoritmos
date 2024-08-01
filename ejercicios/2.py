"""
Solicitar números al usuario hasta que ingrese el cero. 
Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).
"""

numero = int(1)

def sumaDigitos(numero_digitos):
    suma = int(0)
    for i in str(numero_digitos):
        suma += int(i)
    return suma

while(numero != 0):
    numero = int(input("Ingrese un número: "))
    print(f'Suma de sus dígitos: {sumaDigitos(numero)}')
