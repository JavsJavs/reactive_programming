from rx import create
import time

def generador(observer, scheduler):
    observer.on_next('Hola')
    time.sleep(5)
    observer.on_next('Adios')
    observer.on_completed()

observable = create(generador)

observable.subscribe(
    on_next = lambda v: print(f'Recibido: {v}'))