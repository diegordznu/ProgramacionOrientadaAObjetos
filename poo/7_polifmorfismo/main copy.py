import os
from coches import *

#solicitar los datos que posteriormente seran los atributos del objeto
def autos():
    print(f"\n\t Datos del automovil\n")
    marca=input("Introduce la marca del auto: ").upper()
    color=input("Introduce el color del auto: ").upper()
    modelo=input("Introduce el modelo del auto: ").upper()
    velocidad=int(input("Introduce la velocidad del auto: "))
    potencia=int(input("Introduce la potencia del auto: "))
    plazas=int(input("Introduce el numero de plazas del auto: "))

    coche=Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"Datos del Vehiculo: \n Marca:{coche.getMarca()} \n color: {coche.getColor()} \n Modelo: {coche.getModelo()} \n velocidad: {coche.getVelocidad()} \n caballaje: {coche.getCaballaje()} \n plazas: {coche.getPlazas()} ")
def camionetas():
    print(f"\n\t Datos de la camioneta\n")
    marca=input("Introduce la marca de la camioneta: ").upper()
    color=input("Introduce el color de la camioneta: ").upper()
    modelo=input("Introduce el modelo de la camioneta: ").upper()
    velocidad=int(input("Introduce la velocidad de la camioneta: "))
    potencia=int(input("Introduce la potencia de la camioneta: "))
    plazas=int(input("Introduce el numero de plazas de la camioneta: "))

    traccion=input("Introduce el tipo de traccion de la camioneta: ").upper()
    camioneta=(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    cerrada=input("La camioneta es cerrada (si/no): ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False

    coche=Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    print(f"Datos del Vehiculo: \n Marca:{coche.getMarca()} \n color: {coche.getColor()} \n Modelo: {coche.getModelo()} \n velocidad: {coche.getVelocidad()} \n caballaje: {coche.getCaballaje()} \n plazas: {coche.getPlazas()} ")
def camiones():
    print(f"\n\t Datos del camion\n")
    marca=input("Introduce la marca del camion: ").upper()
    color=input("Introduce el color del camion: ").upper()
    modelo=input("Introduce el modelo del camion: ").upper()
    velocidad=int(input("Introduce la velocidad del camion: "))
    potencia=int(input("Introduce la potencia del camion: "))
    plazas=int(input("Introduce el numero de plazas del camion: "))

    eje=int(input("Introduce el numero de ejes del camion: "))
    capacidadCarga=int(input("Introduce la capacidad de carga del camion: "))

    coche=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    print(f"Datos del Vehiculo: \n Marca:{coche.getMarca()} \n color: {coche.getColor()} \n Modelo: {coche.getModelo()} \n velocidad: {coche.getVelocidad()} \n caballaje: {coche.getCaballaje()} \n plazas: {coche.getPlazas()} ")

opcion=1
while opcion!="4":
    os.system("cls")
    opcion=input("\n\t\tMENU PRINCIPAL \n1.- coches\n2.- Camionetas\n3.- Camiones\n4.- Salir \n elige una opcion: ").lower().strip()
    match opcion:
        case "1":
            autos()
            input("presiona una tecla para continuar...")
        case "2":
            camionetas()
            input("presiona una tecla para continuar...")
        case "3":
            camiones()
            input("presiona una tecla para continuar...")
        case "4":
            print("gracias por usar el programa")
        case _:
            print("opcion invalida, intenta de nuevo")






def camionetas():
    print(f"\n\t Datos de la camioneta\n")
    marca=input("Introduce la marca de la camioneta: ").upper()
    color=input("Introduce el color de la camioneta: ").upper()
    modelo=input("Introduce el modelo de la camioneta: ").upper()
    velocidad=int(input("Introduce la velocidad de la camioneta: "))
    potencia=int(input("Introduce la potencia de la camioneta: "))
    plazas=int(input("Introduce el numero de plazas de la camioneta: "))

    traccion=input("Introduce el tipo de traccion de la camioneta: ").upper()
    camioneta=(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    cerrada=input("La camioneta es cerrada (si/no): ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False

    coche=Camionetas(marca,color,modelo,velocidad,potencia,plazas)
    print(f"Datos del Vehiculo: \n Marca:{coche.getMarca()} \n color: {coche.getColor()} \n Modelo: {coche.getModelo()} \n velocidad: {coche.getVelocidad()} \n caballaje: {coche.getCaballaje()} \n plazas: {coche.getPlazas()} ")
def camiones():
    print(f"\n\t Datos del camion\n")
    marca=input("Introduce la marca del camion: ").upper()
    color=input("Introduce el color del camion: ").upper()
    modelo=input("Introduce el modelo del camion: ").upper()
    velocidad=int(input("Introduce la velocidad del camion: "))
    potencia=int(input("Introduce la potencia del camion: "))
    plazas=int(input("Introduce el numero de plazas del camion: "))

    eje=int(input("Introduce el numero de ejes del camion: "))
    capacidadCarga=int(input("Introduce la capacidad de carga del camion: "))

    coche=Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    print(f"Datos del Vehiculo: \n Marca:{coche.getMarca()} \n color: {coche.getColor()} \n Modelo: {coche.getModelo()} \n velocidad: {coche.getVelocidad()} \n caballaje: {coche.getCaballaje()} \n plazas: {coche.getPlazas()} ")


camion=Camiones("VW","Blanco Aperlado","2020",200,180,4,2,"4x4")
print(camion.color, camion.acelerar)

camioneta=Camionetas("VW","Azul","2020",220,180,4,"delantera",True)
print(camioneta.color, camioneta.acelerar)
#coche1=Coches("vw","blanco", "2022", 220, 150,5)
#coche2=Coches("Nissan","azul", "2020", 280, 150,6)'''