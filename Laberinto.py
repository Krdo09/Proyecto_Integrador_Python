from readchar import readkey, key
import os
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

"""
Parte III
Manipulación de la consola mediante la libreria os
"""

def limpiar_terminal(a):
    num = 0
    while True:
      k = readkey()
      if k == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        num += 1
        print(num)
      if num == 50:
        break
