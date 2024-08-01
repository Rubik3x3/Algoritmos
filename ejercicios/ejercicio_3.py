"""
Solicitar números al usuario hasta que ingrese el cero. 
Por cada uno, mostrar la suma de sus dígitos. 
Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
Reutilizar la misma función realizada en el ejercicio 2.
"""

from funciones.sumaDigitos import sumaDigitos

if __name__ == "__main__":

    numero = int(1)
    sumatoria = int(0)
    suma_digitos_total = int(0)

    while(numero != 0):
        numero = int(input("Ingrese un número: "))
        if numero != 0: 
            sumatoria += numero
            suma_digitos_total += sumaDigitos(numero)
            print(f'Suma de sus dígitos: {sumaDigitos(numero)}')

    print(f'Sumatoria Total: {sumatoria}')
    print(f'Suma total de los dígitos de todos los números: {suma_digitos_total}')
