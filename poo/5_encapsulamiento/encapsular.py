import os
os.system("cls")
class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

def __init__(self,color,tamaño):
    self.__color=color
    self.__tamaño=tamaño

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamaño(self):
        return self.__tamaño
    @tamaño.setter
    def tamaño(self,tamaño):
        self.__tamaño=tamaño

def _getAtributoPrivado(self):
    return self.atributo_protegido

def setAtributoPrivado(self,atributo_privado):
    self.__atributo_privado=atributo_privado

#usar los atributos y metodos de acuerdo a su encapsulamiento
objeto=Clase("rojo","grande")
print(f"mi objeto tiene los siguientes atributos: {objeto.color} y {objeto.tamaño}")
print(f"soy el contenido del atributo : {objeto.atributo_publico}")
print(f"soy el contenido del atributo : {objeto._atributo_protegido}")
print(f"soy el contenido del atributo : {objeto.get__atributo_privado}")
objeto.setAtributoPrivado("se ha cambiado el valor del atributo privado")
print(f"soy el contenido del atributo privado: {objeto.getAtributoPrivado()}")