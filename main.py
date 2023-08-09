from Clases import JuegoArchivo
from functools import reduce

def main():
    coordenadas, mapa = JuegoArchivo.archivos2()
    coor_ini = tuple([coordenadas[0], coordenadas[1]])
    coor_final = tuple([int(reduce(lambda result, num: str(result) + str(num), coordenadas[2:4])),
                        int(reduce(lambda result, num: str(result) + str(num), coordenadas[4:6]))])
    j1 = JuegoArchivo(mapa, coor_ini, coor_final)
    j1.loop(j1.matriz())


if __name__ == "__main__":
    main()
