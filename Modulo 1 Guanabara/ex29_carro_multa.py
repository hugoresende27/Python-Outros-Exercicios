vel=float(input("A que velocidade foi apanhado?? --> "))

if (vel>80):
    multa=(vel-80)*7
    print ("MULTADO")
    print ("Foste apanhado com {}km/h de excesso e multado em {} euros".format((vel-80),multa))   


print ("Tenha um bom dia! Dirija em segurança!")