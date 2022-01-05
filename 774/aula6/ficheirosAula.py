import os #importar acções do sistema operativo


dirX = "E:\Other projects\GitHub\MeusProjetos\Python-Outros-Exercicios\\774\\aula6/file1.txt"

f = open(dirX, "r")

print (f.read()) #lê toda a info do ficheiro

#print (f.read(5)) #lê os primeiros 5 chars do ficheiro

#print (f.readline()) #lê linha a linha 1  #deixa um espaço de 1 linha entre cada linha
#print (f.readline()) #lê linha a linha 2

#for x in f:         #percorre o ficheiro linha a linha
    #print (x)       #imprime cada linha individualmente


#f.close()

#posso tbm usar o mecanismo with, dispensa o close()
#with open ("E:\Other projects\GitHub\MeusProjetos\Python-Outros-Exercicios\\774\\aula6/file1.txt", "r") as file:
    #print (file.read())
    
    
with open ("file1.txt", "a") as fi:            # o "a" acrescenta no fim !
    fi.write("\nMais isto acrescentado!")
    
with open ("file1.txt", "w") as fi:            # o "w" acrescenta no principio !
    fi.write("\nIsto vem para o inicio")
    
#with open (dirX, "r") as fi:
     #fi.read()

# f = open(dirX, "a")
# f.write("\nMais isto")

#f.close()

os.remove(dirX)

