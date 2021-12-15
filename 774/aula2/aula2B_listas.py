lista_cores = ["preto","branco","cinza","amarelo",True,25.4]
lista_cores.append("HUGAO")
lista_cores.insert(-1,"Resende")

print (lista_cores[1:3])
#print (len(lista_cores))
if "preto" or "azul" in lista_cores:
    print ("SIM")
else: print("NÃO")

lista_cores[5]="Castanho"
lista_cores[1:2]=["Castanho","azul"]

print (lista_cores)


listaVazio = [1,2,3,4,5,6,7,8,9,10]
print (len(listaVazio))
print (max(listaVazio))
print (min(listaVazio))
print(listaVazio[-4:-1])
print(listaVazio[:-1])
print(listaVazio[-1::-1])
if 10 in listaVazio:
    print ("SIIIM")
    
lista_cores.extend(listaVazio)
lista_cores.pop(4)
lista_cores.remove(3)
#lista_cores.clear()
del lista_cores[0]
print("FINAL ",lista_cores)