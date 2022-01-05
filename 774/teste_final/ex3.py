# Numa competição de ginástica, cada atleta recebe os votos de sete júris. Crie um programa 
# que receba o nome do ginasta e as notas dos sete jurados (Insira as notas numa lista). 
# Calcule e mostre a média e mestre a nota máxima e mínima. No final as notas também 
# devem ser apresentadas por ordem crescente. Utilize uma lista auxiliar para o efeito

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
print ("\033[37;45mMEDIA :: %.2f \033[m"%(sum(nova_lista)/len(lista_notas)))
print(nova_lista)





   