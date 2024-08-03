# Franco Salvador Talarico - 4°3
# Funcion que devuelve la suma de los digitos de un número
def sumaDigitos(numero_digitos):
    suma = int(0)
    for i in str(numero_digitos):
        suma += int(i)
    return suma