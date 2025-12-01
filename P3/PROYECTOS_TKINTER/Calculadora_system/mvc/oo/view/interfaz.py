import tkinter as tk
from controller import funciones
from tkinter import ttk
from tkinter import messagebox
from model import operaciones

class Vista:
    def __init__(self, window):
        window.title("Calculadora")
        window.geometry("1024x768")
        window.resizable(False, False)
        Vista.interfaz_principal(window)
    
    @staticmethod
    def borrarPantalla(window):
        for widget in window.winfo_children():
            if widget != window.nametowidget(window.cget("menu")):
                widget.destroy()
    
    @staticmethod
    def menuPrincipal(window):
        menubar = tk.Menu(window)
        window.config(menu=menubar)
        menu_operaciones = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operaciones", menu=menu_operaciones)
        menu_operaciones.add_command(label="Agregar", command=lambda:Vista.interfaz_principal(window))
        menu_operaciones.add_command(label="Consultar", command=lambda:Vista.interfazConsultar(window))
        menu_operaciones.add_command(label="Cambiar", command=lambda:Vista.interfazCambiar(window))
        menu_operaciones.add_command(label="Borrar", command=lambda:Vista.interfazBorrar(window))
        menu_operaciones.add_separator()
        menu_operaciones.add_command(label="Salir", command=window.quit)
    
    @staticmethod
    def interfaz_principal(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        frame_valores = tk.Frame(window, bg="skyblue")
        frame_valores.propagate(False)
        frame_valores.pack(pady=20)
        
        lbl_1 = tk.Label(frame_valores, text="Ingrese el primer numero:")
        lbl_1.grid(column=0, row=0, padx=10, pady=10)
        
        lbl_2 = tk.Label(frame_valores, text="Ingrese el segundo numero:")
        lbl_2.grid(column=0, row=1, padx=10, pady=10)
        
        num1 = tk.IntVar()
        num2 = tk.IntVar()
        
        entry_1 = tk.Entry(frame_valores, textvariable=num1)
        entry_1.focus()
        entry_1.grid(column=1, row=0, padx=10, pady=10)
        
        entry_2 = tk.Entry(frame_valores, textvariable=num2)
        entry_2.grid(column=1, row=1, padx=10, pady=10)
        
        frame_botones = tk.Frame(window, width=400, height=80, bg="red")
        frame_botones.propagate(False)
        frame_botones.pack(pady=20)
        
        btn_suma = tk.Button(frame_botones, text="SUMA", command=lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "+"))
        btn_suma.grid(row=0, column=0, padx=[5,0])
        
        btn_resta = tk.Button(frame_botones, text="RESTA", command=lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "-"))
        btn_resta.grid(row=0, column=1, padx=5)
        
        btn_div = tk.Button(frame_botones, text="DIVISION", command=lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "/"))
        btn_div.grid(row=0, column=2, padx=5)
        
        btn_mult = tk.Button(frame_botones, text="MULTIPLICACION", command=lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "x"))
        btn_mult.grid(row=0, column=3, padx=[0,5])
        
        btn_salir = tk.Button(window, text="Salir", command=window.quit)
        btn_salir.pack(pady=10)

    @staticmethod
    def interfazBorrar(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        lbl_1 = tk.Label(window, text="Borrar una Operacion")
        lbl_1.pack()
        lbl_id = tk.Label(window, text="ID de la Operacion: ")
        lbl_id.pack()
        
        id = tk.IntVar()
        
        entry_1 = tk.Entry(window, textvariable=id)
        entry_1.focus()
        entry_1.pack()
        
        btn_eliminar = tk.Button(window, text="Eliminar", command=lambda:funciones.Funciones.borrar(id.get()))
        btn_eliminar.pack(pady=10)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.interfaz_principal(window))
        btn_volver.pack(pady=10)
    
    


    @staticmethod
    def interfazConsultar(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        
        lbl_titulo = tk.Label(window, text=".::Listado de Operaciones::.", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=15)
        
        registros = operaciones.Operaciones.consultar()
        if not registros:
            messagebox.showinfo("Consulta", "No hay operaciones registradas en la base de datos.")
            return
        cadena=""
        contador=1
        for registro in registros:
            cadena+=f"Operacion {contador} ID: {registro[0]} Fecha de Creacion: {registro[1]}\nOperacion: {registro[2]} {registro[4]} {registro[3]} = {registro[5]}\n"
            contador+=1
        lbl_registros = tk.Label(window, text=cadena)
        lbl_registros.pack()
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.interfaz_principal(window))
        btn_volver.pack(pady=10)


    @staticmethod
    def interfazCambiar(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)

        lbl_titulo= tk.Label(window, text="Cambiar una Operacion", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=15)

        lbl_cambiar=tk.Label(window, text="Ingresa el ID de la Operacion a cambiar")
        lbl_cambiar.pack(pady=10)
        btn_cambiar=tk.Entry(window)
        btn_cambiar.pack(pady=10)
        btn_eliminar = tk.Button(window, text="Buscar", command=lambda:(id.get()))
        btn_eliminar.pack(pady=10)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.interfaz_principal(window))
        btn_volver.pack(pady=10)

        actualizar=operaciones.Operaciones.actualizar
        if id not in operaciones:
            messagebox.showinfo("Consulta", "No hay operaciones con esa ID")

"""
    @staticmethod
    def interfazConsultar(window):
        # 1. Limpiar la ventana y configurar el menú
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        
        # 2. Título
        lbl_titulo = tk.Label(window, text="Registro de Operaciones", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=15)
        
        # 3. Obtener los datos del modelo
        registros = operaciones.Operaciones.consultar()
        
        if not registros:
            messagebox.showinfo("Consulta", "No hay operaciones registradas en la base de datos.")
            return

        # 4. Crear el Treeview (la tabla)
        
        # Define las columnas
        columnas = ("ID", "Fecha", "Número 1", "Operación", "Número 2", "Resultado")
        tree = ttk.Treeview(window, columns=columnas, show="headings")
        tree.pack(fill='both', expand=True, padx=20, pady=10)

        # Configura los encabezados (headings)
        tree.heading("ID", text="ID")
        tree.heading("Fecha", text="Fecha y Hora")
        tree.heading("Número 1", text="Num 1")
        tree.heading("Operación", text="Signo")
        tree.heading("Número 2", text="Num 2")
        tree.heading("Resultado", text="Resultado")

        # Configura el ancho de las columnas (opcional)
        tree.column("ID", width=50, anchor='center')
        tree.column("Fecha", width=150, anchor='center')
        tree.column("Número 1", width=80, anchor='center')
        tree.column("Operación", width=80, anchor='center')
        tree.column("Número 2", width=80, anchor='center')
        tree.column("Resultado", width=100, anchor='center')

        # 5. Insertar los datos en el Treeview
        for registro in registros:
            # Los registros de la BD deben estar en el orden correcto para la tabla
            # Los datos de la consulta SQL son: (id, fecha, n1, n2, signo, resultado)
            # En Python se insertan como: (id, fecha, n1, signo, n2, resultado)
            # ¡Cuidado con el orden de n2 y signo en tu tabla!
            
            # Formatear la fecha para que se vea mejor (el [1] es el campo fecha)
            fecha_formateada = registro[1].strftime("%Y-%m-%d %H:%M:%S")

            # Insertar la fila
            # Datos: (id, fecha, n1, signo, n2, resultado)
            # Los campos de registro son: (id, fecha, n1, n2, signo, resultado)
            tree.insert("", tk.END, values=(
                registro[0], 
                fecha_formateada, 
                registro[2], # n1
                registro[4], # signo
                registro[3], # n2 
                registro[5]  # resultado
            ))
        
        # 6. Botón Volver
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.interfaz_principal(window))
        btn_volver.pack(pady=10)"""