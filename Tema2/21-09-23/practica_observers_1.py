from rx import create, operators
from rx.core import Observer
import requests
#7ad3d9b4

class Printer(Observer):
    def on_next(self, content):
        print(content)
    def on_completed(self):
        print('Done')

def observer_teclado(observer, scheduler):
    while 1:
        msg = input('\nIntroduce la pelicula a buscar:\t')
        if msg:            
            print('Buscando...')
            params = { 'apikey': '7ad3d9b4', 's': msg}
            content = requests.get(f'https://www.omdbapi.com/', params)
            for movie in content.json().get('Search') or []:
                observer.on_next(movie)
        else:
            observer.on_completed()
            return

observable = create(observer_teclado)

cadena = observable.pipe(
    operators.filter(lambda v: v["Type"] == 'movie'),
    operators.map(lambda v: "(" + v["imdbID"] + ")" + " - " + v["Title"] + ": " + v["Poster"] + " (" + v["Year"] + ")")
)

cadena.subscribe(Printer())

