"""
Sin ejecutar el siguiente programa, determinar cuál es 
la salida en pantalla si se ingresan los valores x=6, y=7:
"""

def coordenadaZ(x,y):
  x=x+10
  y=y+15
  return x+y
 
#programa principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
  z=coordenadaZ(x,y)
  x=x+1
  y=y+1
print(x," . ",y)

"""
RESPUESTA:

Pasos:
- INICIO
- Se ingresa x=6
- Se ingresa y=7
- Ciclo for:
--
-- 1er Ciclo:
--- Funcion coordenadaZ:
---- x=x+10 -> x=6+10 -> [ x=16 ]
---- y=y+15 -> y=7+15 -> [ y=22 ]
---- z=x+y -> [ z=38 ]
--- Siguientes instrucciones:
---- x=x+1 -> x=7
---- y=y+1 -> y=
--
-- 2do Ciclo:
--- Funcion coordenadaZ:
---- x=x+10 -> x=7+10 -> [ x=17 ]
---- y=y+15 -> y=8+15 -> [ y=23 ]
---- z=x+y -> [ z=40 ]
--- Siguientes instrucciones:
---- x=x+1 -> x=8
---- y=y+1 -> y=9
--
-- 3er Ciclo:
--- Funcion coordenadaZ:
---- x=x+10 -> x=8+10 -> [ x=18 ]
---- y=y+15 -> y=9+15 -> [ y=24 ]
---- z=x+y -> [ z=42 ]
--- Siguientes instrucciones:
---- x=x+1 -> x=9
---- y=y+1 -> y=10
- Mostrar 'x . y'
- [ x=9 y=10 ]
- Muestra '9 . 10'
- FIN
--
"""