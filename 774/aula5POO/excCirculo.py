import math

class Circulo:
    def __init__(self,x1,y1,raio):            
        self.x1=x1
        self.y1=y1
        self.raio=raio
    
    def getRaio(self):
        return self.raio
    
    def perimetro(self):
        return 2*math.pi*self.raio
    
    def area(self):
        return math.pi*math.pow(self.raio,2)

    def aumentaRaio(self,aumento):          #actualiza o raio, sem return
        self.raio+=aumento

    def raioMario(self,circ):
        if self.raio>circ.getRaio():return True        #chama o getRaio de circ, o obj concreto
        else:return False
        
c1=Circulo(1,1,5)
c2=Circulo(5,2,3)
print ("Area c1: %.2f" %c1.area())
print ("Area c2: %.2f" %c2.area())
print ("Perimetro c1: %.2f" %c1.perimetro())
print ("Perimetro c2: %.2f" %c2.perimetro())

print ("Raio c1 %d" %c1.getRaio())
print ("Raio c2 %d" %c2.getRaio())

c2.aumentaRaio(2)
print ("Raio c2 %d" %c2.getRaio())

print("c1 maior") if (c1.getRaio() > c2.getRaio())  else print("c2 maior")