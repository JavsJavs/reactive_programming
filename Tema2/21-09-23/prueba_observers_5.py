from rx import of, operators

fuente = of('Hola', 'Adios')

cadena = fuente.pipe(
    operators.map(lambda v: f'-{v.upper()} seniora'),
    operators.map(lambda v: f'-Hola senior {v}'))

cadena.subscribe(lambda v: print(f'Recibido: {v}'))