"""
Franco Salvador Talarico - 4°3

Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.

Precondición: 
el formato del nombre de los socios será: nombre apellido. 
Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. 
Si un socio tuviera más de un apellido, el usuario sólo ingresará uno.

Se debe validar que el número de DNI tenga 7 u 8 dígitos. 
En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.

Por cada socio se debe imprimir su identificador único, el cual estará formado por: 
el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. 

Ejemplo:
Nombre: Alba María Linares
DNI: 25834910
Alba7258
"""

from funciones.listaPalabras import listaPalabras
from funciones.validarDNI import validarDNI
from funciones.sumaDigitos import sumaDigitos

def primerosNDigitos(numero,n_digitos):
    while numero >= 1*(10**n_digitos):
        numero = numero // 10
    return numero

def generarIdentificador(nombre_completo,dni):
    identificador = ""
    primer_nombre = listaPalabras(nombre_completo)[0]
    apellido = ""
    if(len(listaPalabras(nombre_completo)) == 2):
        apellido = listaPalabras(nombre_completo)[1]
    elif(len(listaPalabras(nombre_completo)) == 3):
        segundo_nombre = listaPalabras(nombre_completo)[1]
        apellido = listaPalabras(nombre_completo)[2]       
    identificador += primer_nombre
    letras_apellido = str(len(apellido))
    identificador += letras_apellido
    dni3 = primerosNDigitos(dni,3)
    identificador += str(dni3)

    return identificador


nombre_completo = " "

while(nombre_completo != ""):
    nombre_completo = str(input("Ingrese el nombre completo: "))
    if(nombre_completo == ""):
        break
    dni = int(input("Ingrese el DNI: "))

    while(validarDNI(dni) == False):
        dni = int(input("Ingrese un correcto DNI: "))

    print(generarIdentificador(nombre_completo,dni))