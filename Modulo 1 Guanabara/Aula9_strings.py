print ("#"*120)

s ="Curso em video python"
print (s[0:21:2])       #começa no 0, vai até ao fim, de 2 em 2
print (s[:5])           #começa no 0, pára no 5
print (s[9::3])         #começa no 9, vai até ao fim, de 3 em 3

s1='Hugo'
print (s1[1:3])         #começa no 1 vai até ao 2

print (s1[0:21:2])      #começa no 0, vai até ao fim(ou indice 20) de 2 em 2

print (s1[:2])          #começa no 0 pára no 1
print (s1[1:])          #começa no 1, vai até ao fim
print (s1[1::2])        #começa no 1, vai até ao fim, de 2 em 2

print (len(s))          #comprimento da string
print (s.count('o',0,13))#quantos 'o' existem de 0 a 12

print (s.find('deo'))      #onde começou o 'deo'
print (s.find("Hugo"))

print ('Curso' in s)        #vai resultar True ou False, se 'Curso' existe na string ou não
print (s.replace('Curso','Formação'))   #replace de Curso por formação, apenas aqui na var em baixo volta a 'curso'
print (s.upper())           #print em MAIUSCULAS
print (s.lower())           #print em minusculas
print (s.capitalize())      #joga tudo em minusculo e depois a primeira em MAIUSCULO
print (s.title())           #analisa as palavras e cada palavra a primeira letra fica MAIUSCULA
print (s.strip())           #elimina todos os espaços inúteis no inicio e no fim da string
print (s.rstrip())          #elimina somente os espaços do lado direito no fim da string
print (s.lstrip())          #elimina somente os espaços do lado esquerdo no fim da string

print (s.split())           #criar uma lista, cada palavra num index
print ('-'.join(s))         #print da string com '-' no lugar dos espaços
print ("#".join(s1))        #print da string "Hugo" com "#" em vez de espaço, "H#u#g#o"

print ("##"*50)
frase = "Hugo Emanuel Teixeira Resende"
print (frase.lower().find("emanuel"))       #ao colocar tudo em lower(), posso procurar por palavra em minusculas
print (frase.split())
divi=frase.split()      #criei um objeto divi com a lista das palavras da frase
print (divi[2])         #print da palavra do index 2
print (divi[3][0])      #print da letra index 3 da palavra do index 3