# Franco Salvador Talarico - 4°3
# Saber si un DNI es válido o no (tiene 7 u 8 dígitos)
def validarDNI(dni):
    dni_mod = dni
    digitos = int(0)
    while(dni_mod > 1):
        dni_mod = dni_mod / 10
        digitos += 1
    if(digitos == 7 or digitos == 8):
        return True
    else:
        return False