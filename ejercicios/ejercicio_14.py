"""
Franco Salvador Talarico - 4°3

Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo 
la primera letra de cada palabra a mayúscula y las demás letras a minúscula, dejando 
inalterados los demás caracteres. Precondición: el separador de palabras es el espacio: " ".

Agregar doctests con suficientes casos de prueba para validar que la función 
retorna el valor esperado ante distintos argumentos.
"""

import doctest

def titulo(string):
    """
    Ejemplos:
    >>> titulo("hola como estas")
    'Hola Como Estas'
    >>> titulo("hola   mundo ")
    'Hola   Mundo '
    >>> titulo(" este es un texto")
    ' Este Es Un Texto'
    >>> titulo("me gusta python")
    'Me Gusta Python'
    >>> titulo("hol")
    'Hol'
    """
    siguiente_mayuscula = True
    palabra_con_mayuscula = False
    string_modificado = ""
    for i in string:
        if(i.isalpha()) and palabra_con_mayuscula == False:
            siguiente_mayuscula = True
        if(siguiente_mayuscula):
            string_modificado += i.upper()
            siguiente_mayuscula = False
            palabra_con_mayuscula = True
        else:
            string_modificado += i.lower()
        if(i == ' '):
            palabra_con_mayuscula = False
    return string_modificado

doctest.testmod()

texto = str(input("Ingrese un texto: "))

print(titulo(texto))
