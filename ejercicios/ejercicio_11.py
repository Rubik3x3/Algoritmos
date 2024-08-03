"""
Escribir una función que, dado un número de DNI, retorne True 
si el número es válido y False si no lo es. 
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
"""

def validarDNI(dni):
    dni_mod = dni
    digitos = int(0)
    while(dni_mod > 1):
        dni_mod = dni_mod / 10
        digitos += 1
    if(digitos == 7 or digitos == 8):
        return True
    else:
        return False

dni = int(input("Ingrese un DNI: "))
if(validarDNI(dni)):
    print(f'El DNI: {dni} es válido.')
else:
    print(f'El DNI: {dni} NO es válido.')


          