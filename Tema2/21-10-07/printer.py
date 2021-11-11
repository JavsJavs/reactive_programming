import rx

class Printer(rx.core.Observer):
    def on_next(self, data):
        print(f'Recibido{data}')
    def on_error(self, status):
        print(status)