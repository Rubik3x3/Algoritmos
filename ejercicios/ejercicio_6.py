def factorial(numero):
    factorial = int(1)
    for i in range(1,numero+1):
        factorial = factorial*i
    return factorial

total_numeros = int(0)
numero = int(1)
while(numero != 0):
    numero = int(input("Ingrese un número: "))
    print(f'El factorial de {numero} es {factorial(numero)}')
print(f'Total de números: {total_numeros}')