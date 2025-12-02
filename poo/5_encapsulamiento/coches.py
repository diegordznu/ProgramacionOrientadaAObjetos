import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #metodo constructor para inicializar los valores de los atributos a la hora de crear o instanciar un objeto de la clase
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
     self.__marca= marca
     self.__color= color
     self.__modelo= modelo
     self.__velocidad= velocidad
     self.__caballaje= caballaje
     self.__plazas= plazas
    #crear los metodos setters y getters .-estos metodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos a traves de estos
    #metodos...digamos que es la manera adecuada y recomendada para solicitar un valor (get) y o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a través de un objeto
    #en teoría se debería crear un metodo getter y setter por cada atributo que contenga la clase
    #los metodos get siempre regresan valor, es decir, el valor de la propiedad a traves del return
    #por otro lado el metodo set siempre recibe parametros par cambiar modificar el valor de la propiedad
    #Metodos o acciones o funciones que hace el objeto 

    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    def getVelocidad(self):
        return self.__velocidad

    def setCaballaje(self, caballaje):
        self.__caballaje = caballaje

    def getCaballaje(self):
        return self.__caballaje
    
    def setPlazas(self, plazas):
        self.__plazas = plazas

    def getPlazas(self):
        return self.__plazas
    
    #acciones que realiza el objeto
    def acelerar(self):
        return "haz acelerado"
    def frenar(self):
        return "haz frenado"



#Fin definir clase

#Crear un objetos o instanciar la clase
coche1=Coches("vw","blanco", "2022", 220, 150,5)
coche2=Coches("Nissan","azul", "2020", 280, 150,6)


#coche1.setMarca("VW")
#coche1.setColor("Blanco")
#coche1.setModelo("2022")
#coche1.setVelocidad(220)
#coche1.setCaballaje(150)
#coche1.setPlazas(5)
#coche1.setNumserie("29381")


print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

#coche2=Coches()
#coche2.setMarca("Nissan")
#coche2.setColor("Azul")
#coche2.setModelo("2020")
#coche2.setVelocidad("180")
#coche2.setCaballaje(150)
#coche2.setPlazas(6)

print(f"\nDatos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")