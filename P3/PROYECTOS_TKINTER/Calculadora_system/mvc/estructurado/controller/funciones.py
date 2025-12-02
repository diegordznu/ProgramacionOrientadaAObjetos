from tkinter import messagebox

#Control App o Controller
def operacion(tipo,numero1,numero2):
    if tipo=="+":
        res=numero1+numero2
        op="+"
    elif tipo=="-":
        res=numero1-numero2
        op="-"
    elif tipo=="X":
        res=numero1*numero2
        op="X"
    elif tipo=="/":
        res=numero1/numero2
        op="/"
    messagebox.showinfo(title=tipo,message=f"{numero1} {op} {numero2} = {res}",icon="info")
    
