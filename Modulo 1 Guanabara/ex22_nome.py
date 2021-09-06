nome = input("Qual o seu nome?? --> ").strip()
print ("Nome em Maiusculas",nome.upper())
print ("Nome em minusculas",nome.lower())



print ("O tamanho do nome é {}".format(len(nome)-nome.count(" ")))
lista=nome.split()
print ("O primeiro nome é ",lista[0], " e tem ",len(lista[0]),"letras")

print ("O seu primeiro nome tem {} letras".format(nome.find(" "))) #vai contar até ao primeiro espaço
