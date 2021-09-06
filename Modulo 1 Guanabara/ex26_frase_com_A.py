frase=input("Digite uma frase --> ").strip().upper()

print ("A letra A aparece {} vezes".format(frase.count("A")))
print ("A letra A aparece a primeira vez na posição {}".format(frase.find("A")+1))

print ("A letra A aparece a última vez na posição {}".format(frase.rfind("A")+1))