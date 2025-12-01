from tkinter import *
from tkinter import messagebox
class View:
    def __init__ (self, ventana):
        self.ventana=ventana
        ventana.title("..: Notas System :..")
        ventana.geometry("800x600")
        ventana.resizable(0,0)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def login_accion(self, ventana):
        messagebox.showinfo(icon="info", title="Exito!", message="Accion realizada con exito")
        self.menu_principal(ventana)

    def notas_accion(self, ventana):
        messagebox.showinfo(icon="info", title="Exito!", message="Accion realizada con exito")
        self.menu_notas(ventana)


    def menu_principal(self, ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Menu Principal ::..", justify=CENTER ).pack(pady=10)
        btn_registro=Button(ventana, text="1.- Registro", command=lambda: self.registro(ventana)).pack(pady=15)
        btn_login=Button(ventana, text="2.- Login", command=lambda: self.login(ventana)).pack(pady=15)
        btn_salir=Button(ventana, text="3.- Salir", command=ventana.quit).pack(pady=15)

    def registro(self, ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Registro de Usuario ::..", justify=CENTER).pack(pady=10)

        lbl_nombre=Label(ventana, text="Nombre: ", justify=CENTER).pack(pady=15)
        entry_nombre=Entry(ventana)
        entry_nombre.focus()
        entry_nombre.pack(pady=15)

        lbl_apellido=Label(ventana, text="Apellido:", justify=CENTER).pack(pady=15)
        entry_apellido=Entry(ventana).pack(pady=15)

        lbl_email=Label(ventana, text="email:", justify=CENTER).pack(pady=15)
        entry_email=Entry(ventana).pack(pady=15)


        lbl_contrasena=Label(ventana, text="Contraseña:", justify=CENTER).pack(pady=15)
        entry_contrasena = Entry(ventana, show="*") 
        entry_contrasena.pack(pady=15)

        btn_registrar=Button(ventana, text="Registrar", justify=CENTER, command=lambda: self.login_accion(ventana)).pack(pady=10)
        btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: self.menu_principal(ventana)).pack(pady=10)

    def login(self, ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Login ::..", justify=CENTER).pack(pady=10)

        lbl_email=Label(ventana, text="email:", justify=CENTER).pack(pady=15)
        entry_email=Entry(ventana)
        entry_email.pack(pady=10)
        entry_email.focus()

        lbl_contrasena=Label(ventana, text="Contraseña:", justify=CENTER).pack(pady=15)
        entry_contrasena=Entry(ventana, show="*")
        entry_contrasena.pack(pady=10)

        btn_login=Button(ventana, text="Ingresar", justify=CENTER, command=lambda: self.menu_notas(ventana)).pack(pady=10)
        btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: self.menu_principal(ventana)).pack(pady=10)


    def menu_notas(self, ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Bienvenido (NOmbre) (Apellidps), has iniciado sesion ::..", justify=CENTER ).pack(pady=10)
        btn_crear=Button(ventana, text="1.- Crear", command=lambda:self.crear_nota(ventana)).pack(pady=10)
        btn_mostar=Button(ventana, text="2.- Mostrar", command=lambda:self.registro_nota(ventana)).pack(pady=10)
        btn_cambiar=Button(ventana, text="3.- Cambiar", command=lambda:self.modificar_nota(ventana)).pack(pady=10)
        btn_eliminar=Button(ventana, text="4.- Eliminar", command=lambda: self.borrar_nota(ventana)).pack(pady=10)
        btn_regresar=Button(ventana, text="1.- Regresar", command=lambda: self.menu_principal(ventana)).pack(pady=10)

    def crear_nota(self, ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: Crear nota ::..", justify=CENTER).pack(pady=10)

        lbl_title=Label(ventana, text="Titulo: ", justify=CENTER).pack(pady=15)
        entry_title=Entry(ventana)
        entry_title.focus()
        entry_title.pack(pady=15)

        lbl_descripcion=Label(ventana, text="Descripcion: ", justify=CENTER).pack(pady=15)
        entry_descripcion=Entry(ventana)
        entry_descripcion.pack(pady=15)

        btn_guardar=Button(ventana, text="Guardar", justify=CENTER, command=lambda: self.notas_accion(ventana)).pack(pady=10)
        btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: self.menu_notas(ventana)).pack(pady=10)

    def registro_nota(self, ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="(Nombre), tus notas son:", justify=CENTER).pack(pady=10)

        filas=""
        registros=[("1", "100", "Nota1", "Descripcion de la nota 1", "2025-11-24")]
        num_nota=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"Nota: {num_nota}\n id: {fila[0]} .- titulo: {fila[2]}     Fecha de creacion: {fila[4]}\n Descripcion: {fila[3]}   "
                num_nota+=1
        else:
            messagebox.showwarning(icon="warning", title="...No existen notas para este usuario...")

        lbl_resultado=Label(ventana, text=f"{filas}")
        lbl_resultado.pack(pady=10)

        btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: self.menu_notas(ventana)).pack(pady=10)

    def modificar_nota(self, ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: (Nombre) (Apellido), vamos a modificar una nota ::..", justify=CENTER).pack(pady=10)

        lbl_nota=Label(ventana, text="ID de la nota a cambiar: ", justify=CENTER).pack(pady=10)
        entry_nota=Entry(ventana)
        entry_nota.focus()
        entry_nota.pack(pady=10)

        lbl_new_title=Label(ventana, text="Nuevo titulo: ", justify=CENTER).pack(pady=10)
        entry_new_title=Entry(ventana)
        entry_new_title.pack(pady=10)

        lbl_new_desc=Label(ventana, text="Nueva descripcion: ", justify=CENTER).pack(pady=10)
        entry_new_desc=Entry(ventana)
        entry_new_desc.pack(pady=10)

        btn_guardar=Button(ventana, text="Guardar", justify=CENTER, command=lambda: self.notas_accion(ventana)).pack(pady=10)
        btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: self.menu_notas(ventana)).pack(pady=10)

    def borrar_nota(self, ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..:: (Nombre) (Apellido), vamos a borrar una nota ::..", justify=CENTER).pack(pady=10)

        lbl_nota=Label(ventana, text="ID de la nota a eliminar: ", justify=CENTER).pack(pady=10)
        entry_id=Entry(ventana)
        entry_id.focus()
        entry_id.pack(pady=10)

        btn_eliminar=Button(ventana, text="Eliminar", justify=CENTER, command=lambda: self.notas_accion(ventana)).pack(pady=10)
        btn_volver=Button(ventana, text="Volver", justify=CENTER, command=lambda: self.menu_notas(ventana)).pack(pady=10)









        


        




