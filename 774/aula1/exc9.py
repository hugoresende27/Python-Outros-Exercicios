# Programa que pede o dia da semana e indica se o utilizador escreveu um dia do fim de semana 
#ou um dia útil. Utilize uma estrutura match-case.

dia = int(input("Dia da semana--> "))
match dia:
    case 1:print ("DOMINGO")
    case 2:print ("SEGUNDA")
    case 3:print ("TERCA")
    case 4:print ("QUARTA")
    case 5:print ("QUINTA")
    case 6:print ("SEXTA")
    case 7:print ("SÁBADO")
    case _:print ("INVÁLIDO")