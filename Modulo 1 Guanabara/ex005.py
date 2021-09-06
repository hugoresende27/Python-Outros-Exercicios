n = int(input("Valor:::"))
print ("O valor {} tem antecessor {} e sucessor {}".format(n,  (n-1)  ,  (n+1)  ))
print ("No valor {} o dobro é {} o triplo {} e a raiz quadrada {:.2f}".format(n,(n*2),(n*3),(n**(1/2))))

nota1=float(input("nota1:::"))
nota2=float(input("nota2:::"))
print ("A média entre {} e {} é {:.2f}".format(nota1,nota2,((nota1+nota2)/2)))

metros=float(input("Quantos metros:::"))
print ("{} metros é igual a {:.0f} centimetros e {:.0f} milimetros".format(metros,(metros*100),(metros*1000)))