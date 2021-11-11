from os import error
from tkinter import *
from tkinter.ttk import Combobox
from functools import partial

class App:
    def __init__(self):
        self.__contador = 0
        self.__displaytext = ""
        self.window = Tk()
        self.window.title = 'Aplicación Gráfica!'        
        self.lastdisplayed = 'number'
        self.firstNumber = None
        self.secondNumber = None
        self.current_operator = None
        self.result = 0
        # window.maxsize(width=300, height=200)
        # window.minsize(width=100, height=120)
        # window.geometry('800x400')

        def pressedButton(buttonpressed):
            error = False
            self.display
            self.__contador += 1
            if(buttonpressed in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']):                
                if(self.lastdisplayed == 'op'):
                    self.__displaytext = str(buttonpressed)
                else:
                    self.__displaytext += str(buttonpressed)
                self.lastdisplayed = 'number'                
                self.display.configure(text=self.__displaytext)
            else:
                if(self.firstNumber == None):
                    self.firstNumber = int(self.__displaytext)
                    self.first_display.configure(text=self.__displaytext)
                    self.display.configure(text='')
                elif(self.secondNumber == None):
                    self.secondNumber = int(self.__displaytext)
                else:
                    self.__displaytext = "Two operators max"
                    self.display.configure(text=self.__displaytext)
                if(buttonpressed == 'reset'):
                    self.firstNumber = None
                    self.secondNumber = None
                    self.first_display.configure(text='')
                    self.op_display.configure(text='')                    
                    self.display.configure(text='')
                elif(buttonpressed == '='):
                    if(self.current_operator == '+'):
                        self.result = self.firstNumber + self.secondNumber
                    elif(self.current_operator == '-'):
                        self.result = self.firstNumber - self.secondNumber
                    elif(self.current_operator == '*'):
                        self.result = self.firstNumber * self.secondNumber
                    elif(self.current_operator == '/'):
                        if(self.secondNumber == 0):
                            self.display.configure(text='Cannot divide by zero')
                            error = True
                        else:
                            self.result = self.firstNumber / self.secondNumber
                    if(error == False):
                        self.__displaytext = str(self.result)
                        self.display.configure(text=self.__displaytext)
                    self.firstNumber = None
                    self.secondNumber = None
                    self.first_display.configure(text='')
                    self.op_display.configure(text='')
                else:
                    self.current_operator = buttonpressed
                    self.op_display.configure(text=buttonpressed)
                self.lastdisplayed = 'op'

        self.display = Label(text='0', font=('Arial Bold', 36))
        self.display.grid(column=2, row=0, rowspan=2)

        self.first_display = Label(text='', font=('Arial Bold', 36))
        self.first_display.grid(column=0, row=0)

        self.op_display = Label(text='', font=('Arial Bold', 36))
        self.op_display.grid(column=1, row=0)

        self.button7 = Button(text='7', command=partial(pressedButton, '7'), pady=15, padx=20)
        self.button7.grid(column=0, row=2)
        self.button8 = Button(text='8', command=partial(pressedButton, '8'), pady=15, padx=20)
        self.button8.grid(column=1, row=2)
        self.button9 = Button(text='9', command=partial(pressedButton, '9'), pady=15, padx=20)
        self.button9.grid(column=2, row=2)
        self.buttonPlus = Button(text='+', command=partial(pressedButton, '+'), pady=15, padx=20)
        self.buttonPlus.grid(column=3, row=2)

        self.button4 = Button(text='4', command=partial(pressedButton, '4'), pady=15, padx=20)
        self.button4.grid(column=0, row=3)
        self.button5 = Button(text='5', command=partial(pressedButton, '5'), pady=15, padx=20)
        self.button5.grid(column=1, row=3)
        self.button6 = Button(text='6', command=partial(pressedButton, '6'), pady=15, padx=20)
        self.button6.grid(column=2, row=3)
        self.buttonSubstract = Button(text='-', command=partial(pressedButton, '-'), pady=15, padx=20)
        self.buttonSubstract.grid(column=3, row=3)

        self.button1 = Button(text='1', command=partial(pressedButton, '1'), pady=15, padx=20)
        self.button1.grid(column=0, row=4)
        self.button2 = Button(text='2', command=partial(pressedButton, '2'), pady=15, padx=20)
        self.button2.grid(column=1, row=4)
        self.button3 = Button(text='3', command=partial(pressedButton, '3'), pady=15, padx=20)
        self.button3.grid(column=2, row=4)
        self.buttonTimes = Button(text='*', command=partial(pressedButton, '*'), pady=15, padx=20)
        self.buttonTimes.grid(column=3, row=4)

        self.button0 = Button(text='0', command=partial(pressedButton, '0'), pady=15, padx=20)
        self.button0.grid(column=0, row=5)
        self.buttonDivide = Button(text='/', command=partial(pressedButton, '/'), pady=15, padx=20)
        self.buttonDivide.grid(column=1, row=5)
        self.buttonExec = Button(text='=', command=partial(pressedButton, '='), pady=15, padx=46)
        self.buttonExec.grid(column=2, row=5, columnspan=2)
        
        self.buttonReset = Button(text='reset', command=partial(pressedButton, 'reset'), pady=15, padx=46)
        self.buttonReset.grid(column=0, row=6, columnspan=6)

        self.window.mainloop()


if __name__ == '__main__':
    App()
