# Franco Salvador Talarico - 4°3
# Calcular el factorial de un número
def factorial(numero):
    factorial = int(1)
    for i in range(1,numero+1):
        factorial = factorial*i
    return factorial