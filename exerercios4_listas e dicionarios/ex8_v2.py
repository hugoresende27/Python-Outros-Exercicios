alunos={
        " ":" ",
        " ":" ",
        " ":" ",
        " ":" "
    }

print (alunos)

for x in range (4):
    nome= input("Nome? ")
    alunos[nome]=alunos[" "]
for x in range (4):
    nota = float(input("Nota de %s :: "%x))
    alunos[x]=nota

#for x in alunos:
    
    

print (alunos)
#print (sum(alunos.values())/(len(alunos) ) ) 