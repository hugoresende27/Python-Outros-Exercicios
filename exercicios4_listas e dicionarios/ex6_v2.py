dicio = { "Maria": [99887766, 99887755],
          "Pedro": 92345678,
          "Patrícia": 99887711
        }
print (dicio)
quem=input("Qual o nome ?")
if quem in dicio:
    print (dicio[quem])
else:
    print ("Nao existe")
dicio["Pedro"]=666

print (dicio)
dicio["João"] = 65443322
print (dicio)
print(dicio.keys())
dicio.popitem()
print (dicio)