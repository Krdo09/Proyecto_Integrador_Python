import random
from dataclasses import dataclass, field
import os
from readchar import readkey, key
import pickle

"""
Parte IV proyecto integrador
"""

@dataclass
class Juego:
    mapa: str
    coor_ini: tuple[0, 0] = field(default_factory=tuple)
    coor_fin: tuple[int, int] = field(default_factory=tuple)

    def matriz(self):
        matriz = []
        for line in self.mapa.split('\n'):
            matriz.append(list(line))
        return matriz

    @classmethod
    def pantalla(cls, laberinto: list):
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
                if laberinto[py][px] == '.':
                    laberinto[py][px] = 'P'
                    laberinto[py-1][px] = '.'
                    Juego.pantalla(laberinto)
                elif laberinto[py][px] == '#':
                    py -= 1
                    Juego.pantalla(laberinto)
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

    @staticmethod
    def archivos():
        path_mapas = "C:/Users/MrBra/OneDrive/Documentos/Documentos Julián/Clases ProTalento/Trabajos/Proyecto_Integrador/Mapas"
        path_completo = f"{path_mapas}/{random.choice(os.listdir(path_mapas))}"
        with open(f"{path_completo}", "r") as datos:
            while True:
                try:
                    line = datos.readline()

                except:
                    pass

