def sumaDigitos(numero_digitos):
    suma = int(0)
    for i in str(numero_digitos):
        suma += int(i)
    return suma