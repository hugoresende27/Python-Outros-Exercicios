#Programa que calcula a quantidade de valores pares e também impares que existem num 
#conjunto de 5 valores inseridos pelo utilizador.
pares=impares=0

for x in range(5):
    val = int (input("\033[32mQual o nr? --> "))
    if (val %2 == 0):
        pares+=1
    else:
        impares+=1
        
print ("\033[33mPARES %s \033[36mIMPARES %s\033[m" %(pares,impares))