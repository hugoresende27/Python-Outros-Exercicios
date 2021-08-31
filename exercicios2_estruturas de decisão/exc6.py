nome = input("Qual o seu nome? ")
idade = int(input("Qual a idade? "))

licen =input("És licenciado? ")

#se nao tivesse () para fazer a instrução verdadeira bastava colocar s ou S com um valor < 30
if (licen == "s" or licen == "S") and (20<idade<30):
    print ("ACEITE")
else:
    print ("NAO ACEITE")