#  Crie a classe Retangulo com as características seguintes:
# a.Um construtor que recebe como parâmetro as coordenadas (x1,y1,x2,y2) dos 
# extremos da diagonal do retângulo.
# b.Quatro métodos para calcular a base, a altura, o perímetro (2*base+2*altura) e a área 
# do retângulo (base*altura).
# c. Cria uma instância da classe Retangulo com os valores x1=2, y1=1, x2=4 e y2=5.
# d.Calcula a base, a altura, o perímetro e a área da instância da classe Retangulo e mostra 
# o resultado no ecrã


class Retangulo:
    #construtor
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
        
        
        
print ("\033[37;42m PROGRAMA RETÂNGULO\033[m")

r1=Retangulo(int(input("X1->")),int(input("Y1->")),int(input("X2->")),int(input("Y2->")))

print ("BASE :: ",r1.base())
print ("ALTURA :: ",r1.altura())
print ("PERIMETRO :: ",r1.perimetro())
print ("AREA :: ",r1.area())