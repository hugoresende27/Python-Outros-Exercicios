
contagem=0

print ("\033[33;40m PROGRAMA POLICIA - SUSPEITOS\033[m")
p1 = input ("\033[34;47m Telefonou para a vitima? (s/n) :: \033[m").lower()
if p1 == "s":
    contagem+=1

p2 = input ("\033[34;47m Esteve no local do crime? (s/n) :: \033[m").lower()
if p2 == "s":
    contagem+=1

p3 = input ("\033[34;47m Mora perto da vitima? (s/n) :: \033[m").lower()
if p3 == "s":
    contagem+=1

p4 = input ("\033[34;47m Devia para a vitima? (s/n) :: \033[m").lower()
if p4 == "s":
    contagem+=1

p5 = input ("\033[34;47m Já trabalhou com a vitima? (s/n) :: \033[m").lower()
if p5 == "s":
    contagem+=1



match contagem:
    case 2:
        print ("Classificação :: \033[37;46m SUSPEITA \033[m nivel (%d)"%contagem)
    case 3|4:
        print ("Classificação :: \033[37;45m CÚMPLICE \033[m nivel (%d)"%contagem)
    case 5:
        print ("Classificação :: \033[37;41m ASSASSINO \033[m nivel (%d)"%contagem)
    case _:
        print ("Classificação :: \033[37;42m INOCENTE \033[m nivel (%d)"%contagem)
        