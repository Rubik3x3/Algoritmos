# Franco Salvador Talarico - 4°3
# Saber un dígito se encuentra dentro de un número
def ocurrenciaDigito(numero,digito):
   contador=0
   for i in str(numero):
       if(i == str(digito)):
           contador += 1
   return contador