

lista_notas=[]

print ("\033[31;47m PROGRAMA GINÁSTICA\033[m")

nome=input("Qual o teu nome? ::")
for x in range(7):
    nota=float(input("NOTA %s ::" %(x+1)))
    lista_notas.append(nota)

nova_lista=lista_notas.copy()

nova_lista.sort()

print ("\033[30;47m ATLETA :: %s \033[m" %nome)
print ("\033[37;41mNOTA MÁXIMA :: %d \033[m" %nova_lista[-1])
print ("\033[37;44mNOTA MINIMA :: %d \033[m" %nova_lista[0])
print ("\033[37;45mMEDIA :: %.2f \033[m"%(sum(nova_lista)/7))





   