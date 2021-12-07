#Programa que pode a nota do aluno (1 a 5) e indica a sua avaliação qualitativa 
# (Mau, Insuficiente, Suficiente, Bom e Muito Bom)
nota = int(input("Qual a nota? --> "))
match nota:
    case 1:print("Mau")
    case 2:print("Insuficiente")
    case 3:print("Suficiente")
    case 4:print("Bom")
    case 5:print("Muito Bom")