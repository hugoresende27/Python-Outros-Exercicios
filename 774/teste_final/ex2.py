
contagem=0

print ("\033[33;40m PROGRAMA POLICIA - SUSPEITOS\033[m")
p1 = input ("Telefonou para a vitima? (s/n) :: ").lower()
if p1 == "s":
    contagem+=1

p2 = input ("Esteve no local do crime? (s/n) :: ").lower()
if p2 == "s":
    contagem+=1

p3 = input ("Mora perto da vitima? (s/n) :: ").lower()
if p3 == "s":
    contagem+=1

p4 = input ("Devia para a vitima? (s/n) :: ").lower()
if p4 == "s":
    contagem+=1

p5 = input ("Já trabalhou com a vitima? (s/n) :: ").lower()
if p5 == "s":
    contagem+=1


print (contagem)
match contagem:
    case 2:
        print ("Classificação :: \033[37;46m SUSPEITA \033[m")
    case 3|4:
        print ("Classificação :: \033[37;45m CÚMPLICE \033[m")
    case 5:
        print ("Classificação :: \033[37;41m ASSASSINO \033[m")
    case _:
        print ("Classificação :: \033[37;42m INOCENTE \033[m")
        