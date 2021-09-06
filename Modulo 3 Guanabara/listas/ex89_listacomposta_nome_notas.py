
alunos=[]

while True:
    nome=str(input("Nome:: "))    
    nota1=float(input("Nota 1:: "))   
    nota2=float(input("Nota 2:: "))   
    media=(nota1+nota2)/2
    alunos.append( [nome,[nota1,nota2],media] )         #ciar lista composta, com [para o argumento e , separar ]
    res=str(input("Quer continuar ? (S/N)"))
    if res in "nN":
        break

print ("No.  "+"NOME"+" "*10+"MEDIA")
print ("-"*30)
for index, x in enumerate (alunos):                     #imprimir elementos com index, usando enumerate                
    print (index," ",x[0]," "*(13-len(x[0]))   ,  x[2]   )  #print complexo, 
          #index primeiro, espaço e depois o nome x[0], mais um espaço " " e depois o 13-len(nome) para ficar sempre
          # o mesmo espaço no output, parecendo uma tabela, no fim o print da média x[2]  
          
while True:                                     #ciclo infinito

    mostra=int(input("Nota de Qual aluno?? (999 interrompe) :: "))
    for index, x in enumerate (alunos):         #percorrer lista com index e elemento
        if index == mostra:                     #quando o index for igual à opção
            print ("Notas do aluno %s são %s" %(x[0],x[1])) #dá print do nome e das notas do alunos, contido em
                                                           #em x[0](nome) e x[1](notas1,notas2)
    if mostra == 999:                                       #999 para o break
        break
    elif mostra > index:
        print ("Aluno não existe!")

#######################

    