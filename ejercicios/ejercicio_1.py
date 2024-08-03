"""
Franco Salvador Talarico - 4°3

Solicitar al usuario que ingrese su dirección email. 
Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
Una dirección se considerará válida si contiene el símbolo "@".
"""

def validarEmail(email):
    for i in email:
        if i == "@":
            return True
    return False

email_ingresado = str(input("Ingrese su email: "))

if(validarEmail(email_ingresado)):
    print(f'El email {email_ingresado} es válido.')
else:
    print(f'El email {email_ingresado} NO es válido.')