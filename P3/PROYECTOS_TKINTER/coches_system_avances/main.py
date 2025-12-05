from view.menu_principal import MenuPrincipal
from tkinter import *

class App:
    @staticmethod
    def main(ventana):
        view=MenuPrincipal(ventana)

if __name__ == "__main__":
    ventana=Tk()
    App.main(ventana)
    ventana.mainloop()

'''
1er diciembre
1)implementacion de mvc
2)POO
3)INTERFACES:
    3.1 menu_principal()
    3.2 menu_acciones()
    3.3 insertar_autos()

productos entregables:
    estructura del proyecto basado en mvc
    archivo principal main funcionado
    interacción con las interfaces



4 diciembre
4)CONTROLADOR
    1.1 insertar_camionetas()
    1.2 consultar_camionetas()
    1.3 cambiar_camionetas()
    1.4 borrar_camionetas()

'''