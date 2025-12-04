"""
ejercicio practico 2 modelar y diagramar
"""
import os

os.system("cls")

#crear una clase
class Coches:
    def __init__(self,color, marca, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def mostrar_info(self):
        print(f"Coche: {self.marca}, Color: {self.color}, Velocidad: {self.velocidad}")

    def acelerar(self, incremento):
        self.velocidad = self.velocidad + incremento
        return self.velocidad
    
    def frenar(self, decremento):
        self.velocidad = self.velocidad - decremento
        return self.velocidad
        
    def tocar_claxon(self):
        return "PIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"
    
    #INSTACNCIAR OBJETOS DE LA CLASE COCHES
coche1 = Coches("blanco", "toyota", 220)
coche2 = Coches("amrarillo", "Nissan", 180)

print(f"los valores del objeto 1 son: {coche1.marca}, {coche1.color}, {coche1.velocidad})")
print(f"la velocidad original del coche 1 es: {coche1.velocidad} y cambió a: {coche1.acelerar(50)}")

print(f"los valores del objeto 2 son: {coche2.marca}, {coche2.color}, {coche2.velocidad})")
print(f"la velocidad original del coche 2 es: {coche2.velocidad} y cambió a: {coche2.frenar(30)}")