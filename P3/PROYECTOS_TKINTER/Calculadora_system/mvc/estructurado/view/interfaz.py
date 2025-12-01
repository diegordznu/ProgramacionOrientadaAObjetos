from tkinter import messagebox
import tkinter as tk
from controller import funciones

#Interfaz o VIEW
def Interfaz():
    ventana = tk.Tk()
    ventana.title("calculadora basica")
    ventana.geometry("600x600")
    var_num1 = tk.IntVar()
    var_num2 = tk.IntVar()

    var_entrada_n1 = tk.Entry(ventana, textvariable=var_num1, justify="right")
    var_entrada_n1.pack()

    var_entrada_n2 = tk.Entry(ventana, textvariable=var_num2, justify="right")
    var_entrada_n2.pack()

    btn_sumar=tk.Button(ventana,text="+",command=lambda:funciones.operacion("+",var_num1.get(),var_num2.get()))
    btn_sumar.pack()
    btn_restar=tk.Button(ventana,text="-",command=lambda:funciones.operacion("-",var_num1.get(),var_num2.get()))
    btn_restar.pack()
    btn_multiplicar=tk.Button(ventana,text="X",command=lambda:funciones.operacion("X",var_num1.get(),var_num2.get()))
    btn_multiplicar.pack()
    btn_dividir=tk.Button(ventana,text="/",command=lambda:funciones.operacion("/",var_num1.get(),var_num2.get()))
    btn_dividir.pack()

    btn_salir = tk.Button(ventana, text="Salir", command=quit)
    btn_salir.pack()


    ventana.mainloop()