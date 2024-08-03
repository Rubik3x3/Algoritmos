"""
Solicitar al usuario el ingreso de números primos. 
La lectura finalizará cuando ingrese un número que no sea primo. 
Por cada número, mostrar la suma de sus dígitos. 

También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
Al finalizar el programa, mostrar el factorial del mayor número ingresado.
"""

from funciones.esPrimo import esPrimo

numero_primo = int(2)

while(esPrimo(numero_primo)):
    numero_primo = int(input("Ingrese un número primo: "))
