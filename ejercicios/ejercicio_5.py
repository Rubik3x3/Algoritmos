"""
Solicitar al usuario un número entero y luego un dígito. 
Informar la cantidad de ocurrencias del dígito en el número, 
utilizando para ello una función que calcule la frecuencia.
"""

from funciones.ocurrenciaDigito import ocurrenciaDigito

numero=int(input("Ingrese un número: "))
digito=int(input("Ingrese un dígito: "))

print(f'La ocurrencia del dígito {digito} en el número {numero} es {ocurrenciaDigito(numero,digito)}')