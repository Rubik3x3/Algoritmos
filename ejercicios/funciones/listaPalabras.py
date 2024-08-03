def listaPalabras(string):
    longitud = len(string)
    lista_palabras = []

    nueva_palabra = ""
    for i in string:
        if(i != ' '):
            nueva_palabra += i
        else:
            lista_palabras.append(nueva_palabra)
            nueva_palabra = ""
            

    lista_palabras.append(nueva_palabra)
    contador = 1
    while(string[-contador] == ' '):
        lista_palabras.pop()
        contador += 1
    return lista_palabras