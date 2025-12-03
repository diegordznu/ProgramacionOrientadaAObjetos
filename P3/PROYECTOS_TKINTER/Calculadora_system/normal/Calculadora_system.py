'''
    crear una calculadora :
    1.- Dos campos de textos
    2.- 4 botones para las operaciones 
    3.- Mostrar el resultado en una alerta
'''


import tkinter as tk
from tkinter import messagebox

def mostrar_resultados(var_num1, var_num2, resultado, tipo, signo):
    titulo = tipo
    messagebox.showinfo(title=titulo, icon="info", message=f"{var_num1} {signo} {var_num2}= {resultado}")
    

#Control app or controler
def suma(var_num1, var_num2):
    resultado = var_num1 + var_num2
    signo="+"
    tipo="suma"
    mostrar_resultados(var_num1, var_num2, resultado, tipo, signo)

def resta(var_num1, var_num2):
    resultado = var_num1 - var_num2
    signo = "-"
    tipo = "resta"
    mostrar_resultados(var_num1, var_num2, resultado, tipo, signo)

def multiplicacion(var_num1, var_num2):
    resultado = var_num1 * var_num2
    signo = "x"
    tipo = "multiplicacion"
    mostrar_resultados(var_num1, var_num2, resultado, tipo, signo)

def division(var_num1, var_num2):
    try:
        resultado = var_num1 / var_num2
    except ZeroDivisionError:
        messagebox.showerror(title="Error", message="Division por cero no permitida")
        return
    signo = "/"
    tipo = "division"
    mostrar_resultados(var_num1, var_num2, resultado, tipo, signo)


#Interfaz o VIEW
ventana = tk.Tk()
ventana.title("calculadora basica")
ventana.geometry("600x600")
var_num1 = tk.IntVar()
var_num2 = tk.IntVar()

var_entrada_n1 = tk.Entry(ventana, textvariable=var_num1, justify="right")
var_entrada_n1.pack()

var_entrada_n2 = tk.Entry(ventana, textvariable=var_num2, justify="right")
var_entrada_n2.pack()

btn_suma = tk.Button(ventana, text="+", command=lambda: suma(var_num1.get(), var_num2.get()))
btn_suma.pack()

btn_division = tk.Button(ventana, text="/", command=lambda: division(var_num1.get(), var_num2.get()))
btn_division.pack()

btn_multiplicacion = tk.Button(ventana, text="x", command=lambda: multiplicacion(var_num1.get(), var_num2.get()))
btn_multiplicacion.pack()

btn_resta = tk.Button(ventana, text="-", command=lambda: resta(var_num1.get(), var_num2.get()))
btn_resta.pack()

btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
btn_salir.pack()


ventana.mainloop()
btn_salir = tk.Button(ventana, text="Salir", command=quit)


ventana.mainloop()