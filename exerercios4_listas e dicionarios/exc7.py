menu={
    "entremeada": 7,
    "Sardinha":6,
    "Filetes":5.5,
    "Prego":7,
    "Hamburger":5.5
    }

print ("BEM VINDO")
pergunta=input("Deseja ver o menu?(s/n)").lower()
if pergunta == "s":
   

    ############outra maneira

    for x,y in menu.items():
        print (x,y,"€")
    prato=input("Qual o prato?")
    if prato in menu:
        print("Está a ser preparado")
    else:
        print("Prato não existe ou está esgotado")

else:
    print ("Obrigado pela visita")
    exit()
    