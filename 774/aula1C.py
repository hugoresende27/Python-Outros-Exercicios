###########MATCH CASE##################

n = int(input("Nota do aluno--> "))
match n:
    case 1:print("mau")
    case 2:print("insuficiente")
    case 3:print("suficiente")
    case 4:print("bom")
    case 5:print("muito bom")
    case _:print("Nota invalida")#default nao obrigatório