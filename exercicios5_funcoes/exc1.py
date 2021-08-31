import math
#PI=3.14


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
                ****************************
                """)
   
    opcao=int(input("Qual a funcao? :: "))
    raio = float(input("qual o raio?? :: "))
    if opcao == 1:
        print("Área é :: %.2f"%funcao_area(raio))
    elif opcao == 2:
        print ("Perimetro é :: %.2f"%funcao_perimetro(raio))
    elif opcao == 3:
        print ("Diametro é ::  %.2f"%funcao_diametro(raio))
    else:
        print ("Opcao Inválida")
       
menu()