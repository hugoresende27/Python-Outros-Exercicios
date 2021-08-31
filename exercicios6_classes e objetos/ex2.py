import math

class Circulo:
    def __init__(self,x,y,raio):
        self.x=x
        self.y=y
        self.raio=raio

    def getRaio(self):
        return self.raio

    def perimetro (self):
        return (2*math.pi*self.raio)

    def area (self):
        return (math.pi*math.pow(self.raio,2))

    def aum_raio(self,val):
        
        self.raio+=val
        

    def ver_raio(self):
        if self.raio>self.val:
            return ("Raio original é maior")
        else:
            return ("Raio recebido como argumento é maior !!")

circ1=Circulo(1,1,5)
circ2=Circulo(5,2,3)

print ("PERIMETRO 1 :: %.2f" %circ1.perimetro())
print ("PERIMETRO 2 :: %.2f" %circ2.perimetro())
print ("AReA 1 :: %.2f"%circ1.area())
print ("AReA 2 :: %.2f"%circ2.area())

circ1.aum_raio(2)
print ("NOVO RAIO", circ1.getRaio())

if circ1.getRaio()>circ2.getRaio():
    print ("É maior !!!")
else:
    print ("É menor !!!")