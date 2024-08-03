"""
Escribir una función que, dado un número de DNI, retorne True 
si el número es válido y False si no lo es. 
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
"""

from funciones.validarDNI import validarDNI

dni = int(input("Ingrese un DNI: "))
if(validarDNI(dni)):
    print(f'El DNI: {dni} es válido.')
else:
    print(f'El DNI: {dni} NO es válido.')


          