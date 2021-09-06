
nome= input("Qual o nome? --> ").strip()
n=nome.upper()
if "SILVA" in n:
    print ("Tem SILVA")
else:
    print ("NAO TEM SILVA")

print ("O seu nome tem silva?? {}".format("silva" in nome.lower()))