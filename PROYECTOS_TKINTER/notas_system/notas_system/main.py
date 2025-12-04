'''
1.- implementar MVC
2.- Paradigma POO
3.- App de escritorio con interfaz grafica  
'''
from view import view2
from tkinter import *

class App:
    def __init__(self, ventana):
        vista=view2.View(ventana)

if __name__ == '__main__':
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
