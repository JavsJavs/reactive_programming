from rx import create
from rx.core import Observer

class Printer(Observer):
    def on_next(selv, v):
        print(v + '\n')
    def on_completed(self):
        print('Adio feo\n\n')

class Pronter(Observer):
    def on_next(selv, v):
        print('Pues muy bien fiera yo no te hago caso\n')
    def on_completed(self):
        print('Ahi te quedas\n\n')

def observer_teclado(observer, scheduler):
    while 1:
        msg = input('Introduce tu mensaje:\n')
        if msg:
            observer.on_next(msg)
        else:
            observer.on_completed()
            return

observable = create(observer_teclado)

observable.subscribe(Printer())
observable.subscribe(Pronter())