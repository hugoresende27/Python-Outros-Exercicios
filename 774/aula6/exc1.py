#ler todas as linhas de um file e imprimir a maior

f = open ("file1.txt", "r")


tam = 0
maior =""
for x in f:
    if (len(x)>tam):
        tam = len(x)
        maior = x

print (maior)
    
f.close()

with open ("file1.txt", "r") as fi:         
    tam = 0
    maior =""
    for x in fi:
        if (len(x)>tam):
            tam = len(x)
            maior = x

    print (maior)