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

    
    opcao=int(input("Qual a funcao? :: "))
    
    if opcao == 1:
        raio = float(input("qual o raio?? :: "))
        print("Área é :: %.2f"%funcao_area(raio))
      
    elif opcao == 2:
        raio = float(input("qual o raio?? :: "))
        print ("Perimetro é :: %.2f"%funcao_perimetro(raio))
       
    elif opcao == 3:
        raio = float(input("qual o raio?? :: "))
        print ("Diametro é ::  %.2f"%funcao_diametro(raio))
        
    elif opcao ==4:
        exit()
    else:
        print ("Opcao Inválida")
        menu()

opcao =""
while opcao!=4:
    menu()