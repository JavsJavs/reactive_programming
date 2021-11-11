from rx import of

observable = of('Hola', 'Adios')

observable.subscribe(
    on_next = lambda v: print(f'Recibido: {v}'),
    on_completed = lambda: print(f'Ala me piro'))

#observable.subscribe(lambda v: print(f'Rec {v}'))