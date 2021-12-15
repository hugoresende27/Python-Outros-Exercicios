for x in range (1,200,10):#inicio, fim, passo
    print (x,end=" | ")
    
print ("\n"+"-"*30+"\n")

for x in range (200,220):#incio, fim
    print (x,end=" | ")
    
print ("\n"+"-"*30+"\n")

for x in range (20):#fim
    print (x,end=" | ")
else :
    print ("TERMINADO")
    
print ("\n"+"-"*30+"\n")

for x in range (20,-1,-3):
    print (x,end=" | ")
    
print ("\n"+"-"*30+"\n")

for x in range (4):
    print ("\nA",end=" ")       #imprime 1 A
    for y in range (3):
        print ("B", end=" ")  #imprime os 3 B's, depois novamente um 'A'
        
print ("\n"+"-"*30+"\n")

i=1
while (i<6):
   
    if i == 3 : break
    print(i)
    i+=1
    
print ("\n"+"-"*30+"\n")
    
i=1
while (i<6):
    if i == 3 : continue
    print(i)
    i+=1
    