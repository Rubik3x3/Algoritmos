# Franco Salvador Talarico - 4°3
# Saber si un número es primo o no
def esPrimo(numero):
    numeros_divisibles = int(0)
    for i in range(1,numero):
        if(numero % i == 0):
           numeros_divisibles+=1
    if(numeros_divisibles > 2):
        return False
    else:
        return True