print ("\033[7m=\033[m"*100)
print ("\033[7mPrograma MAIOR\033[m")
n=int(input("Escreva NUMERO 1--> "))
n2=int(input("Escreva NUMERO 2--> "))

if n>n2:
    print ("O {} é o maior".format(n))
elif n2>n:
    print ("O maior é o {}".format(n2))
else:
    print ("{} e {} são iguais".format(n,n2))