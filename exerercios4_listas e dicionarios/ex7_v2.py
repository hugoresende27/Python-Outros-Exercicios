menu={ "Entremeada" : 7,
       "Sardinha": 6,
       "Filetes": 5.5,
       "Prego":7,
       "Hamburger":5.5
       }

res=" "
while res!="s" or res!="n":

    res=input("Quer ver o menu (s/n)?? :: ").lower()
    if res == "s":
        for x,y in menu.items():
            print(x,y,"€")
        prato=input("Qual prato? :: ")
        if prato in menu:
            print("A ser pronto")
        else:
            print("ESGOTADO")
    elif res =="n":
        exit()
    else:
        print("Opcao Inválida")
    