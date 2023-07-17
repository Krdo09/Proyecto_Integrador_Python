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

"""
Parte IV
Creación del mapa del laberinto
"""

mapa = """..###################
..#.....#.......#...#
#.#.#.#.###.#######.#
#.#.#.#...........#.#
#.#.#######.#######.#
#.#...#...#.....#.#.#
#.#.###.#.#.#####.#.#
#...#...#.......#...#
###.###.###.#.###.###
#...#...#...#.......#
#.#.###.#####.###.#.#
#.#.#...#...#.#.#.#.#
#####.#.#.#####.#.###
#.....#...#...#.....#
#.#.#####.#.###.###.#
#.#...#...#.#.....#.#
#.###.#.###.###.#.###
#.#.#.#.#.......#...#
#.#.#.#.###.###.#.###
#...#.#.#...#...#...#
###################.#
"""

def matriz(mapa: str):
    matriz = []
    for linea in mapa.split("\n"):
        matriz.append(list(linea))
    punto_final = (len(matriz)-1, len(matriz[0])-2)
    return matriz, punto_final

def pantalla(laberinto):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in laberinto:
        print(i, sep='\n')

def main_loop(mapa):
    laberinto, coor_final = matriz(mapa)
    py, px = 0, 0
    personaje_coor = [py, px]
    laberinto[py][px] = 'P'
    while True:
        k = readkey()
        if k == key.UP:
            py -= 1
            if py != -1:
                if laberinto[py][px] == '.':
                    laberinto[py][px] = 'P'
                    personaje_coor[0] += py
                    pantalla(laberinto)
                elif laberinto[py][px] == '#':
                    py += 1
                    pantalla(laberinto)
            else:
                py += 1
                pantalla(laberinto)
        if k == key.DOWN:
            py += 1
            if laberinto[py][px] == '.':
                laberinto[py][px] = 'P'
                personaje_coor[0] += py
                pantalla(laberinto)
            elif laberinto[py][px] == '#':
                pantalla(laberinto)
                py -= 1
        if k == key.LEFT:
            px -= 1
            if px != -1:
              #Continuar codigo