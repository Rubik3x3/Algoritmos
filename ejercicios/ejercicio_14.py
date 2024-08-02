def titulo(string):
    siguiente_mayuscula = True
    palabra_con_mayuscula = False
    string_modificado = ""
    for i in string:
        if(i != ' ') and palabra_con_mayuscula == False:
            siguiente_mayuscula = True
        if(siguiente_mayuscula):
            string_modificado += i.upper()
            siguiente_mayuscula = False
            palabra_con_mayuscula = True
        else:
            string_modificado += i.lower()
        if(i == ' '):
            palabra_con_mayuscula = False
    return string_modificado

texto = str(input("Ingrese un texto: "))

print(titulo(texto))