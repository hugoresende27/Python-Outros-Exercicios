#. Programa que pede 5 valores ao utilizador e mostra apenas a soma dos valores positivos.
soma=0
for x in range(5):
    val = int (input("Qual o nr? --> "))
    if (val>0):
        soma+=val

print("SOMA %s" %soma)
