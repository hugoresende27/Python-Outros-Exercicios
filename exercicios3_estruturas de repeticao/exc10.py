soma =cont = 0
num = int(input("Insira valor (negativo para Sair)::"))

while num>0:
    if num % 2 == 0:
        soma=soma+num
    cont+=1
    num = int(input("Insira valor (negativo para Sair)::"))


print ("A soma dos valores pares é %s e nr de valores inseridos %s vezes"%(soma,cont))
