nome ="hugo"
idade=32
salario =987.5
print (f"O {nome:20} tem {idade} anos e ganha {salario:.2f}")        #outro método format, f"{nome var}" PYTHON 3.6+
print (f"alinhado à esquerda {nome:<20}")
print (f"alinhado à direita {nome:>20}")
print (f"alinhado ao centro {nome:^20}")
print ("o %s tem %d anos"%(nome,idade))     #metodo print do PYHTON 2

cont=1
while (cont<=10):
    print ("{} - ".format(cont),end="")
    cont+=1
print ("FIM")

soma=0
while True:
    n = int(input("VALOR:: "))
    if n==999:
        break
    soma+=n
print ("A soma vale {}".format(soma))
print (f"a soma é {soma}")


