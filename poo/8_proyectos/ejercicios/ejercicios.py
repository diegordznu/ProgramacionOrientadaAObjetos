n1=int(input("numero #1: "))
n2=int(input("numero #2: "))

class Calculadora:
    def __init__(self,n1,n2):
        self._n1=n1
        self._n2=n2

    def sumar(self):
        return self._n1+self._n2
    def restar(self):
        return self._n1-self._n2
    def multiplicar(self):
        return self._n1*self._n2
    def dividir(self):
        return self._n1/self._n2
    
operacion=Calculadora(n1,n2)
print(operacion.sumar())
print(operacion.restar())
print(operacion.multiplicar())
print(operacion.dividir())