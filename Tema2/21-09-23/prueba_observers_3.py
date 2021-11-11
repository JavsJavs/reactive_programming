from rx import from_

l = [1, 2, 3, 4, 5]
observable = from_(l)

observable.subscribe(
    on_next = lambda v: print(f'Recibido {v}'),
    on_completed = lambda: print('Terminado'),
    on_error = lambda e: print(f'Error detectado: {e}')
)