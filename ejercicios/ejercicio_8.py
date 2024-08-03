"""
Franco Salvador Talarico - 4°3

Solicitar al usuario el ingreso de números primos. 
La lectura finalizará cuando ingrese un número que no sea primo. 
Por cada número, mostrar la suma de sus dígitos. 

También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
Al finalizar el programa, mostrar el factorial del mayor número ingresado.
"""

from funciones.esPrimo import esPrimo
from funciones.sumaDigitos import sumaDigitos
from funciones.ocurrenciaDigito import ocurrenciaDigito
from funciones.factorial import factorial

numero = int(1)
mayor = int(0)

while(numero != 0):
    numero = int(input("Ingrese un número primo: "))
    if(numero != 0):
        if(esPrimo(numero) == False):
            print("El número No es primo.")
            break
        print(f'La suma de los dígitos de {numero} es {sumaDigitos(numero)}.')
        digito = int(input("Ingrese un dígito: "))
        print(f'La ocurrencia del dígito {digito} en el número {numero} es {ocurrenciaDigito(numero,digito)}')
        if(numero > mayor):
            mayor = numero
    else:
        break

print(f"Número mayor ingresado: {mayor}.")
print(f"Factorial de {mayor} es {factorial(mayor)}")
