from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller.camiones_controller import CamionesController

class MenuCamiones:
    def __init__(self, ventana, back_callback):
        self.ventana = ventana
        self.back_callback = back_callback

    def limipia_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Camiones")
        Label(self.ventana, text="CAMIONES", font=("Kalam", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Camion", command=self.insertar_camiones).pack(pady=10)
        Button(self.ventana, text="Consultar Camiones", command=self.consultar_camiones).pack(pady=10)
        Button(self.ventana, text="Actualizar Camion", command=self.actualizar_camiones).pack(pady=10)
        Button(self.ventana, text="Borrar Camion", command=self.borrar_camiones).pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.back_callback).pack(pady=10)

    def insertar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Insertar Camiones")
        Label(self.ventana, text="INSERTAR CAMION", font=("Kalam", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Marca:").pack(); self.cam_marca = Entry(self.ventana); self.cam_marca.pack()
        Label(self.ventana, text="Color:").pack(); self.cam_color = Entry(self.ventana); self.cam_color.pack()
        Label(self.ventana, text="Modelo:").pack(); self.cam_modelo = Entry(self.ventana); self.cam_modelo.pack()
        Label(self.ventana, text="Velocidad:").pack(); self.cam_vel = Entry(self.ventana); self.cam_vel.pack()
        Label(self.ventana, text="Caballaje:").pack(); self.cam_cab = Entry(self.ventana); self.cam_cab.pack()
        Label(self.ventana, text="Plazas:").pack(); self.cam_plazas = Entry(self.ventana); self.cam_plazas.pack()
        # Campos Específicos
        Label(self.ventana, text="Número de Ejes:").pack(); self.cam_eje = Entry(self.ventana); self.cam_eje.pack()
        Label(self.ventana, text="Capacidad Carga (Kg):").pack(); self.cam_carga = Entry(self.ventana); self.cam_carga.pack()

        def guardar_camion():
            if self.cam_marca.get() == "":
                messagebox.showwarning("Error", "Faltan datos")
                return

            exito = CamionesController.insertar(
                self.cam_marca.get(), self.cam_color.get(), self.cam_modelo.get(),
                self.cam_vel.get(), self.cam_cab.get(), self.cam_plazas.get(),
                self.cam_eje.get(), self.cam_carga.get()
            )
            if exito:
                messagebox.showinfo("Éxito", "Camión guardado correctamente")
                self.menu_acciones_camiones()
            else:
                messagebox.showerror("Error", "Error al guardar camión")

        Button(self.ventana, text="Guardar", command=guardar_camion).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camiones).pack(pady=10)

    def consultar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Consultar Camiones")
        Label(self.ventana, text="LISTADO CAMIONES", font=("Times New Roman", 24,"bold")).pack(pady=20)

        # Conexión real al modelo
        registros = CamionesController.consultar()
        
        cadena = ""
        if not registros:
            cadena = "No hay camiones registrados."
        else:
            for registro in registros:
                # id, color, marca, modelo, velocidad, caballaje, plazas, eje, capacidadCarga
                cadena += f"ID: {registro[0]} | Marca: {registro[2]} | Modelo: {registro[3]} | Ejes: {registro[7]} | Carga: {registro[8]}\n"

        Label(self.ventana, text=cadena, justify=LEFT).pack(pady=10)
        Button(self.ventana, text="Volver", command=self.menu_acciones_camiones).pack(pady=10)

    def actualizar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Actualizar Camion")
        Label(self.ventana, text="ACTUALIZAR CAMION", font=("Kalam", 24,"bold")).pack(pady=20)
        Label(self.ventana, text="ID a actualizar:").pack(); self.cam_id_upd = Entry(self.ventana); self.cam_id_upd.pack()
        registros = CamionesController.consultar()
        
        cadena=""
        if not registros:
            cadena = "No hay camiones registrados."
        else:
            for registro in registros:
                # Ajustado a tu SQL: id, color, marca, modelo, velocidad, caballaje, plazas
                # Nota: Verifica el orden de columnas en tu BD, aquí asumo el orden estándar del SELECT *
                cadena += f"ID: {registro[0]} | Marca: {registro[1]} | Color: {registro[2]} | Modelo: {registro[3]} | Vel: {registro[4]} | Caballaje: {registro[5]} | Plazas: {registro[6]} | Eje: {registro[7]} | Capacidad {registro[8]} \n"
        
        lbl_registros = Label(self.ventana, text=cadena, justify=LEFT)
        lbl_registros.pack(pady=10)

        Label(self.ventana, text="Nueva marca:").pack(); self.cam_marca_upd = Entry(self.ventana); self.cam_marca_upd.pack()
        Label(self.ventana, text="Nuevo color:").pack(); self.cam_color_upd = Entry(self.ventana); self.cam_color_upd.pack()
        Label(self.ventana, text="Nuevo modelo:").pack(); self.cam_modelo_upd = Entry(self.ventana); self.cam_modelo_upd.pack()
        Label(self.ventana, text="Nueva velocidad:").pack(); self.cam_vel_upd = Entry(self.ventana); self.cam_vel_upd.pack()
        Label(self.ventana, text="Nuevo caballaje:").pack(); self.cam_cab_upd = Entry(self.ventana); self.cam_cab_upd.pack()
        Label(self.ventana, text="Nuevas plazas:").pack(); self.cam_plazas_upd = Entry(self.ventana); self.cam_plazas_upd.pack()
        Label(self.ventana, text="Nuevo eje:").pack(); self.cam_eje_upd = Entry(self.ventana); self.cam_eje_upd.pack()
        Label(self.ventana, text="Nueva capacidad de carga:").pack(); self.cam_carga_upd = Entry(self.ventana); self.cam_carga_upd.pack()


        def actualizar_camion():
            if CamionesController.actualizar(
                self.cam_id_upd.get(),
                self.cam_marca_upd.get(),
                self.cam_color_upd.get(),
                self.cam_modelo_upd.get(),
                self.cam_vel_upd.get(),
                self.cam_cab_upd.get(),
                self.cam_plazas_upd.get(),
                self.cam_eje_upd.get(),
                self.cam_carga_upd.get()
            ):
                messagebox.showinfo("Éxito", "Camión actualizado correctamente")
                self.menu_acciones_camiones()
            else:
                messagebox.showerror("Error", "Error al actualizar el camión")

        Button(self.ventana, text="Actualizar", command=actualizar_camion).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camiones).pack(pady=10)

    def borrar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Borrar Camion")
        Label(self.ventana, text="BORRAR CAMION", font=("Kalam", 24,"bold")).pack(pady=20)
        registros = CamionesController.consultar()
        
        cadena=""
        if not registros:
            cadena = "No hay camiones registrados."
        else:
            for registro in registros:
                # Ajustado a tu SQL: id, color, marca, modelo, velocidad, caballaje, plazas
                # Nota: Verifica el orden de columnas en tu BD, aquí asumo el orden estándar del SELECT *
                cadena += f"ID: {registro[0]} | Color: {registro[2]} | Marca: {registro[1]} | Modelo: {registro[3]} | Vel: {registro[4]} | Caballaje: {registro[5]} | Plazas: {registro[6]} | Eje: {registro[7]} | Capacidad {registro[8]} \n"
        
        lbl_registros = Label(self.ventana, text=cadena, justify=LEFT)
        lbl_registros.pack(pady=10)

        Label(self.ventana, text="ID a eliminar:").pack(); self.cam_id_del = Entry(self.ventana); self.cam_id_del.pack()

        def eliminar_camion():
            if CamionesController.borrar(self.cam_id_del.get()):
                messagebox.showinfo("Éxito", "Camión eliminado")
                self.menu_acciones_camiones()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el camión")

        Button(self.ventana, text="Borrar", command=eliminar_camion).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camiones).pack(pady=10)
