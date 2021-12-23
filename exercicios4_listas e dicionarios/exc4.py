lista =[]
acima_media = []
soma=entrada=0

for x in range (5):
    entrada = (int(input("Insira um nr:: ")))
    lista.append (entrada)
    soma+=entrada
print ("a. --> ",lista)
print ("b. o maximo é --> %s e o minimo é --> %s" %(max(lista),min(lista)) )
media = soma/5
print ("c. a soma é --> %s e a média é --> %.1f" %(soma,media))

for x in lista:
    if x>media:
        acima_media.append (x)
print ("d. valores acima da media são  ---> %s" %acima_media)

valor = float(input("e. Introduza um valor para verificar se está na lista :: "))
if valor in lista:print ("O valor está na lista!!")
else:print("O valor não está...")
      