r="S"
while r=="S":
    r=(input("Quer continuar? (s/n) --> ")).upper()
print ("FIM")

r1="n"
while r1 =="n":
    r1=input("Quer sair ? (s/n) -->").lower()
print ("FIM 2")

n=1
pares = impares = 0

while (n!=0):  
    n=int(input("Digite um nr--> "))
    if n!=0:            #este if vai prevenir q o 0 quando introduzido seja contabilizado como par
        if n%2==0:      #so é feito se n != 0
            pares+=1
        else:
            impares+=1

print ("Digitou {} números, {} pares e {} impares".format((pares+impares),pares,impares))#outra solução seria pares-1