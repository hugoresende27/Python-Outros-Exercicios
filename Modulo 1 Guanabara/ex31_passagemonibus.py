km=float(input("Quantos Km's? --> "))
if (km<200):
    preco=0.5*km
    print ("{}km vai custar {} euros".format(km,preco))
else:
    preco=0.45*km
    print ("{}km vai custar {} euros".format(km,preco))
