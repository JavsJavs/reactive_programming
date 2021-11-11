import asyncio
import time
import random

DURACION_PARTIDA = 60
NUMERO_OPONENTES = 24
TIEMPO_MAESTRO = 0.00005
TIEMPO_ALUMNO = 0.0005

async def chess_game(id):
    i = 0
    while(i < DURACION_PARTIDA):
        if(i % 2 == 0):
            print("Partida " + str(id) + " async. Turno del maestro (" + str(i) + ")")
            await asyncio.sleep(TIEMPO_MAESTRO)
        else:
            print("Partida " + str(id) + " async. Turno del alumno (" + str(i) + ")")
            await asyncio.sleep(TIEMPO_ALUMNO)
        i += 1
    print("Partida " + str(id) + " async finalizada.")


def chess_game_sync(oponentes):
    for oponente in range(oponentes):
        i = 0
        while(i < DURACION_PARTIDA):
            if(i % 2 == 0):
                print("Partida " + str(oponente + 1) + " sync. Turno del maestro (" + str(i) + ")")
                time.sleep(TIEMPO_MAESTRO)
            else:
                print("Partida " + str(oponente + 1) + " sync. Turno del alumno (" + str(i) + ")")
                time.sleep(TIEMPO_ALUMNO)
            i += 1
        print("Partida " + str(oponente + 1) + " sync finalizada.")


async def main():
    t = time.time()
    chess_game_sync(NUMERO_OPONENTES)
    tiempo_sync = (f'Tiempo de ejecucion: {time.time() - t} segundos')

    t = time.time()
    await asyncio.gather(*(chess_game(n + 1) for n in range(int(NUMERO_OPONENTES))))
    tiempo_async = (f'Tiempo de ejecucion: {time.time() - t} segundos')

    print("\n\nSYNC\n" + tiempo_sync + "\n")
    print("ASYNC\n" + tiempo_async + "\n")

asyncio.run(main())