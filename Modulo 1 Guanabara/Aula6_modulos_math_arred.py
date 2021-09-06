import math
print ("="*100)
valor=float(input("introduza o valor --> "))
raiz = math.sqrt(valor)
elevado = math.pow(valor,2)
fat=math.factorial(int(valor))


print ("A raiz quadrada é {:.3f}".format(raiz))
print ("O valor elevado a ² é {}".format(elevado))
print ("O fatorial é {}".format(fat))

print ("O valor arredondado em ceil é {:.3f}".format(math.ceil(raiz)))
print ("O valor arredondado em floor é {:.3f}".format(math.floor(raiz)))
print ("O valor arredondado em trunc é {:.3f}".format(math.trunc(raiz)))
