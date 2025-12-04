from tkinter import *
from tkinter import ttk
from model import coches
from tkinter import messagebox

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Gestion de Coches")
        self.ventana.geometry("1150x900")
        self.ventana.resizable(False, False)
        
        self.menuprincipal()

    def limipia_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menuprincipal(self):
        self.limipia_ventana()
        self.ventana.title("Menu Principal")
        
        frame_menu = Frame(self.ventana)
        frame_menu.pack(expand=True)

        Label(frame_menu, text="GESTION DE COCHES", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(frame_menu, text="Coches", command=self.menu_acciones).pack(pady=10)
        Button(frame_menu, text="Camionetas", command="").pack(pady=10)
        Button(frame_menu, text="Camiones", command="").pack(pady=10)

        Button(frame_menu, text="Salir", command=self.ventana.quit).pack(pady=10)

    def menu_acciones(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Autos")
        Label(self.ventana, text="AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Autos", command=self.insertar_autos).pack(pady=10)
        Button(self.ventana, text="Consultar Autos",command=self.consultar_autos).pack(pady=10)
        Button(self.ventana, text="Actualizar Autos", command=self.cambiar_autos).pack(pady=10)
        Button(self.ventana, text="Borrar Autos", command=self.borrar_autos).pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.menuprincipal).pack(pady=10)

    def insertar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Insertar Autos")
        Label(self.ventana, text="INSERTAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Marca:").pack(pady=10)
        entry_marca = Entry(self.ventana)
        entry_marca.pack()

        Label(self.ventana, text="Color:").pack(pady=10)
        entry_color = Entry(self.ventana)
        entry_color.pack()

        Label(self.ventana, text="Modelo:").pack(pady=10)
        entry_modelo = Entry(self.ventana)
        entry_modelo.pack()

        Label(self.ventana, text="Velocidad:").pack(pady=10)
        entry_velocidad = Entry(self.ventana)
        entry_velocidad.pack()

        Label(self.ventana, text="Caballaje:").pack(pady=10)
        entry_caballaje = Entry(self.ventana)
        entry_caballaje.pack()

        Label(self.ventana, text="Plazas:").pack(pady=10)
        entry_plazas = Entry(self.ventana)
        entry_plazas.pack()

        Button(self.ventana, text="Guardar", command=lambda: self.guardar_auto(entry_color, entry_marca, entry_modelo, entry_velocidad, entry_caballaje, entry_plazas)).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def guardar_auto(self, entry_color, entry_marca, entry_modelo, entry_velocidad, entry_caballaje, entry_plazas):
        color = entry_color.get()
        marca = entry_marca.get()
        modelo = entry_modelo.get()
        velocidad = entry_velocidad.get()
        caballaje = entry_caballaje.get()
        plazas = entry_plazas.get()

        success = coches.Autos.insertar(color, marca, modelo, velocidad, caballaje, plazas)
        if success:
            messagebox.showinfo("Éxito", "Auto guardado correctamente.")
            self.menu_acciones()
        else:
            messagebox.showerror("Error", "No se pudo guardar el auto. Revisa la consola para más detalles.")

    def consultar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Consultar Autos")
        Label(self.ventana, text="LISTADO DE AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

    
        
        registros = coches.Autos.consultar()
        if not registros:
            messagebox.showinfo("Consulta", "No hay autos registradas en la base de datos.")
            return
        cadena=""
        contador=1
        for registro in registros:
            cadena+=f"Auto {contador} ID: {registro[0]} Marca: {registro[1]} Color: {registro[2]} Modelo: {registro[4]} Velocidad: {registro[3]} Caballaje: {registro[5]}\n"
            contador+=1
        lbl_registros = Label(self.ventana, text=cadena)
        lbl_registros.pack()
        
        btn_volver = Button(self.ventana, text="Volver", command=self.menu_acciones)
        btn_volver.pack(pady=10)

    def cambiar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Cambiar Autos")
        Label(self.ventana, text="CAMBIAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        registros = coches.Autos.consultar()
        if not registros:
            messagebox.showinfo("Consulta", "No hay autos registradas en la base de datos.")
            return
        cadena=""
        contador=1
        for registro in registros:
            cadena+=f"Auto {contador} ID: {registro[0]} Marca: {registro[1]} Color: {registro[2]} Modelo: {registro[4]} Velocidad: {registro[3]} Caballaje: {registro[5]}\n"
            contador+=1
        lbl_registros = Label(self.ventana, text=cadena)
        lbl_registros.pack()

        Label(self.ventana, text="Introduce el ID del auto que deseas cambiar:").pack(pady=10)
        entryid=Entry(self.ventana)
        entryid.pack()

        Label(self.ventana, text="ACTUALIZAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Marca:").pack(pady=10)
        entry_marca = Entry(self.ventana)
        entry_marca.pack()

        Label(self.ventana, text="Color:").pack(pady=10)
        entry_color = Entry(self.ventana)
        entry_color.pack()

        Label(self.ventana, text="Modelo:").pack(pady=10)
        entry_modelo = Entry(self.ventana)
        entry_modelo.pack()

        Label(self.ventana, text="Velocidad:").pack(pady=10)
        entry_velocidad = Entry(self.ventana)
        entry_velocidad.pack()

        Label(self.ventana, text="Caballaje:").pack(pady=10)
        entry_caballaje = Entry(self.ventana)
        entry_caballaje.pack()

        Label(self.ventana, text="Plazas:").pack(pady=10)
        entry_plazas = Entry(self.ventana)
        entry_plazas.pack()

        Button(self.ventana, text="Guardar", command=lambda: self.actualizar_auto(entryid.get(), entry_color, entry_marca, entry_modelo, entry_velocidad, entry_caballaje, entry_plazas)).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def actualizar_auto(self, id_coche, entry_color, entry_marca, entry_modelo, entry_velocidad, entry_caballaje, entry_plazas):
        color = entry_color.get()
        marca = entry_marca.get()
        modelo = entry_modelo.get()
        velocidad = entry_velocidad.get()
        caballaje = entry_caballaje.get()
        plazas = entry_plazas.get()

        success = coches.Autos.actualizar(id_coche, color, marca, modelo, velocidad, caballaje, plazas)
        if success:
            messagebox.showinfo("Éxito", "Auto actualizado correctamente.")
            self.menu_acciones()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el auto. Revisa la consola para más detalles.")

    def borrar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Borrar Autos")
        Label(self.ventana, text="BORRAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Introduce el ID que deseas eliminar:").pack(pady=10)
        entryid=Entry(self.ventana)
        entryid.pack()

        Button(self.ventana, text="Borrar", command=lambda: coches.Autos.eliminar(entryid.get())).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)
