"""
Escribir una función que, dado un string, retorne la longitud de la última palabra. 
Se considera que las palabras están separadas por uno o más espacios. 
También podría haber espacios al principio o al final del string pasado por parámetro.
"""

def longitudUltimaPalabra(string):
    longitud = len(string)
    lista_palabras = []

    nueva_palabra = ""
    for i in string:
        if(i != ' '):
            nueva_palabra += i
        else:
            lista_palabras.append(nueva_palabra)
            nueva_palabra = ""
    lista_palabras.append(nueva_palabra)
    ultima_palabra = lista_palabras[-1]
    longitud_ultima_palabra = len(ultima_palabra)
    return longitud_ultima_palabra
texto = str(input("Ingrese un texto: "))

print(f'La longitud de la última palabra es {longitudUltimaPalabra(texto)}')