km=float(input("Quantos Km? --> "))
dias=int(input("Quantos dias? -->"))
preco = (60*dias)+(0.15*km)
print ("Percorreu {:.1f}km em {} dias tem a pagar {:.2f} € ".format(km,dias,preco))