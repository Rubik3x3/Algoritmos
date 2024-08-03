"""
Franco Salvador Talarico - 4°3

Escribir una función que, dado un string, retorne la longitud de la última palabra. 
Se considera que las palabras están separadas por uno o más espacios. 
También podría haber espacios al principio o al final del string pasado por parámetro.
"""

from funciones.listaPalabras import listaPalabras

def longitudUltimaPalabra(string):
    
    lista_palabras = listaPalabras(string)
    ultima_palabra = lista_palabras[-1]
    longitud_ultima_palabra = len(ultima_palabra)
    return longitud_ultima_palabra
texto = str(input("Ingrese un texto: "))

print(f'La longitud de la última palabra es {longitudUltimaPalabra(texto)}')