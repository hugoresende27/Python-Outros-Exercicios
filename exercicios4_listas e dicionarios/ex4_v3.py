lista=[]

for x in range (5):
    lista.append(int(input("NR :: ")))
print (lista)
print ("MIN :: %d e MAX :: %d"%(min(lista),max(lista)))
print ("MEDIA :: %d" %(sum(lista)/len(lista)))
media = (sum(lista)/len(lista))
for x in lista:
    if x>media:
        print ("Maiores media :: ",x)

valor=int(input("VALOR::"))

if valor in lista:
    print ("SIIIIIIIIIIIIIIIIM")
else:
    print ("NAAAAAAAAAAAAAAAOOO")