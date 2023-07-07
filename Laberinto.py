from readchar import readkey, key
"Parte I"

nombre_jugador = input("Ingresar el nombre del jugador: ")
print("Bienvenido al juego,", nombre_jugador)

"""
Parte II
Bucle infinito, detecta que tecla se pulsa y se cierra con la flecha arriba
"""

while True:
  k = readkey()
  if k == key.UP:
    break
  else:
    print(k)
