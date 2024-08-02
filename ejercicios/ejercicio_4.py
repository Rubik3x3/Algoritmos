"""
Requerir al usuairio que ingrese un número entero e informar si es primo o no,
utilizando una función booleana que lo decida.
"""

def esPrimo(numero):
    numeros_divisibles = int(0)
    for i in range(1,numero):
        if(numero % i == 0):
           numeros_divisibles+=1
    if(numeros_divisibles > 2):
        return False
    else:
        return True
numero = int(input("Ingrese un número: "))

if(esPrimo(numero)):
    print(f'El número {numero} es primo.')
else:
    print(f'El número {numero} NO es primo.')