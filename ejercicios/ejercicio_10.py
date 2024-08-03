"""
El siguiente programa debería imprimir el número 2 si se le 
ingresan como valores x=5, y=1 pero en su lugar imprime 5. 
¿Qué hay que corregir?

CÓDIGO CON ERRORES:

def maximo(a,b):
  if x>y:
    return x
  else:
    return y

 
def minimo(a,b):
  if x<y:
    return x
  else:
    return y

 
#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))
"""

#CÓDIGO CORREGIDO

def maximo(a,b):
  if a>b:
    return a
  else:
    return b
 
def minimo(a,b):
  if a<b:
    return a
  else:
    return b
 
#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

"""
RESPUESTA:

El problema que tiene es que en las funciones definidas como minimo() y maximo()
el nombre de los parametros es 'a' y 'b' y dentro de las funciones se utilizan variables
no definidas ('x' e 'y'). 

Se podria solucionar cambiando el nombre de los parametros ('x' en vez de 'a' e 'y' en vez de b)
o también cambiando los nombres de las variables dentro de la función 'x' e 'y' por 'a' y 'b'
dejando los nombres de los parametros en 'a' y 'b'.

- VERIFICADO
"""