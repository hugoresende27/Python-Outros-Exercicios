print ("="*50)

n=int(input("Tabuada do :::"))
for x in range (1,11):
    print ("{} X {} = {}".format(n,x,(n*x)))

d=float(input("Quantos reais tens???  --> R$ "))
print ("com {} reais podes comprar {:.2f} dólares".format (d,(d/5.38)))
print ("com {} reais podes comprar {:.2f} euros".format (d,(d/6.30 )))