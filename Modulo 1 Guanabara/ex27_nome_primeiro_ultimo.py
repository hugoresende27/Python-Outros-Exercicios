nome=input("Nome completo ---> ").strip()
n=nome.upper().split()
#print (n)

print ("Primeiro nome ---> {}".format(n[0]))
print ("Último nome ---> {}".format(n[-1]))

print ("Bem vindo {} {}".format(n[0],n[-1]))

print ("Ultimo nome de outra maneira {}".format(n[len(n)-1]))       #comprimento -1 dá o ultimo index
