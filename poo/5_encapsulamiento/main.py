import os
os.system("cls")
from coches import *

#solicitar los datos que posteriormente seran los atributos del objeto
num_coches=int(input("Cuantos coches tienes: "))
for i in range(0,num_coches):
    print(f"\n\t Datos del automovil{i+1}\n")
    marca=input("Introduce la marca del auto: ").upper()
    color=input("Introduce el color del auto: ").upper()
    modelo=input("Introduce el modelo del auto: ").upper()
    velocidad=int(input("Introduce la velocidad del auto: "))
    potencia=int(input("Introduce la potencia del auto: "))
    plazas=int(input("Introduce el numero de plazas del auto: "))

coche=Coches(marca,color,modelo,velocidad,potencia,plazas)
print(f"Datos del Vehiculo: \n Marca:{coche.getMarca()} \n color: {coche.getColor()} \n Modelo: {coche.getModelo()} \n velocidad: {coche.getVelocidad()} \n caballaje: {coche.getCaballaje()} \n plazas: {coche.getPlazas()} ")

#coche1=Coches("vw","blanco", "2022", 220, 150,5)
#coche2=Coches("Nissan","azul", "2020", 280, 150,6)