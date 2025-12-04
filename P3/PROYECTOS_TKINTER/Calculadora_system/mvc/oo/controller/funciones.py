import tkinter as tk
from tkinter import messagebox
from model import operaciones

class Funciones:
    @staticmethod
    def operaciones(num1, num2, simbolo):
        if simbolo == "+":
            op = num1 + num2
            tipo = "SUMA"
        elif simbolo == "-":
            op = num1 - num2
            tipo = "RESTA"
        elif simbolo == "x":
            op = num1 * num2
            tipo = "MULTIPLICACION"
        elif simbolo == "/":
            if num2 == 0:
                messagebox.showerror(message="No se puede dividir entre 0")
                op = "ERROR"
            else:
                op = num1 / num2
                tipo = "DIVISION"
        if op == "ERROR":
            pass
        else:
            resultado=messagebox.askquestion(message=f"{num1} {simbolo} {num2} = {op}\n\n¿Deseas guardar en la base de datos?",icon="question", title=tipo)
            if resultado=="yes":
                operaciones.Operaciones.insertar(num1, num2, simbolo, op)
                messagebox.showinfo(title="Insertar", message="Se ha insertado la operacion correctamente.")
    
    @staticmethod
    def borrar(id):
        respuesta = operaciones.Operaciones.eliminar(id)
        if respuesta:
            messagebox.showinfo(title="ELiminacion", message="Se ha eliminado la operacion correctamente.")
        else:
            messagebox.showinfo(title="Error", message="Ha ocurrido un error al eliminar el registro")