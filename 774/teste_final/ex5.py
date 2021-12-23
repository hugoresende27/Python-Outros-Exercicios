class Retangulo:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    
    def base (self):
        return self.x2-self.x1

    def altura (self):
        return self.y2-self.y1
    
    def perimetro (self):
        return (2*self.base()+2*self.altura())
        
    
    def area (self):
        return (self.base()*self.altura())
        
        
r1=Retangulo(2,1,4,5)
print ("BASE :: ",r1.base())
print ("ALTURA :: ",r1.altura())
print ("PERIMETRO :: ",r1.perimetro())
print ("AREA :: ",r1.area())