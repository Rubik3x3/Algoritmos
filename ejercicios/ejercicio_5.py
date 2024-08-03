"""
Solicitar al usuario un número entero y luego un dígito. 
Informar la cantidad de ocurrencias del dígito en el número, 
utilizando para ello una función que calcule la frecuencia.
"""

def ocurrenciaDigitoEnNumero(numero,digito):
   contador=0
   for i in str(numero):
       if(i == str(digito)):
           contador += 1
   return contador

numero=int(input("Ingrese un número: "))
digito=int(input("Ingrese un dígito: "))

print(f'La ocurrencia del dígito {digito} en el número {numero} es {ocurrenciaDigitoEnNumero(numero,digito)}')