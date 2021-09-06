tempo=int(input("Quantos anos tem o seu carro?? --> "))
print ("CARRO NOVO" if tempo<=3 else "CARRO VELHO")
print ("--FIM--")

nome=str(input("Qual o seu nome?")).lower().strip()
if nome == "hugo":
    print ("Que nome lindo")
else:
    print ("Nome normal")

print ("Bem vindo {}".format(nome))