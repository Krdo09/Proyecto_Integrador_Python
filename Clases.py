import random
from dataclasses import dataclass, field
import os
from readchar import readkey, key
from functools import reduce

"""
Parte IV proyecto integrador
"""

@dataclass
class Juego:
    mapa: str
    coor_ini: tuple[int, int] = field(default_factory=tuple)
    coor_fin: tuple[int, int] = field(default_factory=tuple)

    def matriz(self):
        matriz = []
        for line in self.mapa.split('\n'):
            matriz.append(list(line))
        return matriz

    @staticmethod
    def pantalla(laberinto: list):
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in laberinto:
            print("".join(fila), sep='\n')

    def loop(self, laberinto: list):
        py, px = self.coor_ini
        laberinto[py][px] = 'P'
        Juego.pantalla(laberinto)
        while True:
            k = readkey()
            if k == key.UP:
                py -= 1
                if py != -1 and laberinto[py][px] == '.':
                    laberinto[py][px] = 'P'
                    laberinto[py+1][px] = '.'
                    Juego.pantalla(laberinto)
                elif py == -1 or laberinto[py][px] == '#':
                    py += 1
                    Juego.pantalla(laberinto)
            if k == key.DOWN:
                py += 1
                if py != len(laberinto):
                    if laberinto[py][px] == '.':
                        laberinto[py][px] = 'P'
                        laberinto[py-1][px] = '.'
                        Juego.pantalla(laberinto)
                    elif laberinto[py][px] == '#':
                        py -= 1
                        Juego.pantalla(laberinto)
                else:
                    py -= 1
            if k == key.LEFT:
                px -= 1
                if px != -1 and laberinto[py][px] == '.':
                    laberinto[py][px] = 'P'
                    laberinto[py][px+1] = '.'
                    Juego.pantalla(laberinto)
                elif px == -1 or laberinto[py][px] == '#':
                    px += 1
                    Juego.pantalla(laberinto)
            if k == key.RIGHT:
                px += 1
                if laberinto[py][px] == '.':
                    laberinto[py][px] = 'P'
                    laberinto[py][px-1] = '.'
                    Juego.pantalla(laberinto)
                elif laberinto[py][px] == '#':
                    px -= 1
                    Juego.pantalla(laberinto)
            if tuple([py, px]) == self.coor_fin:
                print('Has ganado')
                break

@dataclass
class JuegoArchivo(Juego):

    #Lectura de mapas almacenados en archivos con utilizando un ciclo
    @staticmethod
    def archivos():
        path_mapas = "C:/Users/MrBra/OneDrive/Documentos/Documentos Julián/Clases ProTalento/Trabajos/Proyecto_Integrador/Mapas"
        path_completo = f"{path_mapas}/{random.choice(os.listdir(path_mapas))}"
        map_string = ""
        with open(f"{path_completo}", "r") as datos:
            for line in datos:
                map_string += line
        return map_string.strip()

    #Lectura de mapas almacenados en archivos utilizando programación funcional
    @staticmethod
    def archivos2():
        path_mapas = "C:/Users/MrBra/OneDrive/Documentos/Documentos Julián/Clases ProTalento/Trabajos/Proyecto_Integrador/Mapas"
        path_completo = f"{path_mapas}/{random.choice(os.listdir(path_mapas))}"
        with open(f"{path_completo}", "r") as datos:
            map_string = datos.readlines()
        character_coor = list(map(lambda num: int(num), filter(lambda num: num != ' ' and num != '\n', map_string[0])))
        final_mapa = reduce(lambda string, line: string + line, map_string[1:])
        return character_coor, final_mapa

    def matriz(self):
        return list(map(list, self.mapa.split()))
