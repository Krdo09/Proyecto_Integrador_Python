from Clases import Juego, JuegoArchivo
from Laberinto import mapa
def main():
    j1 = JuegoArchivo(mapa, (0, 0), (20, 19))
    #JuegoArchivo.archivos()
    j1.loop(j1.matriz())


if __name__ == "__main__":
    main()
