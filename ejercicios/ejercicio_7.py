from funciones.sumaDigitos import sumaDigitos

numero = int(1)
contador = 0

mayor = int(0)
menores_de_10 = int(0)

while(numero != 0):
    numero = int(input("Ingrese un número: "))
    numDigitos = sumaDigitos(numero)
    if(contador == 0):
        mayor = numDigitos
    else:
        if(numDigitos > mayor):
            mayor = numDigitos
    if numDigitos < 10:
        menores_de_10 += 1
    contador += 1

print(f'Mayor: {mayor}\nMenores de 10: {menores_de_10}')
