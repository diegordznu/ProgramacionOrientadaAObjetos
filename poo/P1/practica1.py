"""
ejercicio practico 2 modelar y diagramar
"""
import os

os.system("cls")

#crear una clase
class Coches:

    marca = marca
    color = color
    modelo = modelo
    velocidad = velocidad
    caballaje = caballaje
    plazas = plazas

    def mostrar_info(self):
        print(f"Coche: {self.marca}, Color: {self.color}, Modelo: {self.modelo}, Velocidad: {self.velocidad}, Caballaje: {self.caballaje}, Plazas: {self.plazas}")

    def acelerar(self, incremento):
        pass
    
    def frenar(self, decremento):
        pass
    
    #INSTACNCIAR OBJETOS DE LA CLASE COCHES
coche1 = Coches("VW", "blanco", 2020, 220, 150, 5)
coche2 = Coches("Nissan", "amarillo", 2020, 180, 150, 6)

print(f"los valores del objeto 1 son: {coche1.marca}, {coche1.color}, {coche1.velocidad})")
print(f"la velocidad original del coche 1 es: {coche1.velocidad} y cambió a: {coche1.acelerar(50)}")

print(f"los valores del objeto 2 son: {coche2.marca}, {coche2.color}, {coche2.velocidad})")
print(f"la velocidad original del coche 2 es: {coche2.velocidad} y cambió a: {coche2.frenar(30)}")

