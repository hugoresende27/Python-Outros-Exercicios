txt = "Python, a linguagem, de AI, e Python do futuro aaaa!!"

print( "CONTA O NUMERO DE ::", txt.count("a",0,10) ) #pesquisa todos os "a" de txt , value, start , end

print ("TERMINA COM :: ",txt.endswith("aa!!"))   #verifica se txt termina com value, start, end

print ("POSICAO DA PRIMEIRA LETRA DE FIND:: ",txt.find("AI",10,-1))       #verifica se txt tem o valor e devolve a posição value, start, end

lista = ["Hugo", "Resende", "Emanule", "Teixeira"]

print ("\n-->".join(lista)) #especifica o caracter separador

txt2 = "ola AMIGOS!"
print (txt2.lower())
print (txt2.upper())

print (txt.replace("Python", "PHP",1))        #susbtitui a ocorrencia, oldvalue, newvalue, count(quantas ocorrencias vai substituir)

print ("LISTA SEPARADA A CADA ,::", txt.split(", "))        #separa a string numa lista, ", " separa os elementos
print ("LISTA SEPARADA A CADA espaço ::", txt.split())      #separa numa lista, sem argumentos separa a cada espaço