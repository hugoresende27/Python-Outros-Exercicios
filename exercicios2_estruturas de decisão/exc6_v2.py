nome= input("nome:")
idade=int(input("idade:"))
lic=input("licenciado:")

if idade< 30 and (lic=="s" or lic=="S"):
    print( "%s Aceite" %nome)
else:
    print("%s Não Aceite" %nome)
