#1. Crie o seguinte programa:
# a. Crie uma função que permita mostrar ao utilizador o seguinte output:
# b.Crie uma função que devolve o valor da área em que o valor do raio é passado como 
# argumento: area = PI * r2
# c. Crie uma função que devolve o valor do perimetro do círculo em que o valor do raio é 
# passado como argumento: perimetro = 2 PI * r
# d.Crie uma função que devolve o valor do diametro do círculo em que o valor do raio é 
# passado como argumento: diametro = 2 * r
# e. O programa deve pedir ao utilizador o raio do círculo e qual a informação que pretende 
# obter (1, 2 ou 3), mostrando de seguida o resultado correspondente
import math

def funcao_area(raio):
    area=math.pi*(math.pow(raio,2))
    return area
    #return math.pi*(raio**2)

def funcao_perimetro(raio):
    perimetro=2*math.pi*raio
    return perimetro

def funcao_diametro(raio):
    diametro = 2* raio
    return diametro

def menu():
    print ("""
                ***************************
                1- Área de círculo
                2- Perimetro Circulo
                3- Diametro Circulo
                4- Sair
                ****************************
                """)

   
menu() 
r=float(input("Qual o raio? "));
opcao=int(input("Qual a funcao? :: "))
match (opcao):
    case 1:
        print ("RAIO: %.2f" %funcao_area(r))
    case 2:
        print ("RAIO: %.2f" %funcao_perimetro(r))
    case 3:
        print ("RAIO: %.2f" %funcao_diametro(r))
    case 4:
        exit()