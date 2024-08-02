def titulo(string):
    siguiente_mayuscula = True
    string_modificado = ""
    for i in string:
        if(i != ' '):
            siguiente_mayuscula = True
        if(siguiente_mayuscula):
            string_modificado += i.upper()
            siguiente_mayuscula = False
        else:
            string_modificado += i.lower()
    return string_modificado
texto = "hola cOmO eStAS ABC"

print(titulo(texto))