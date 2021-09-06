cidade= input("Qual o nome da cidade? --> ").strip().lower()
c=cidade.upper()
d=c.split()
print (d)
if (d[0]=="SANTO"):
    print ("Começa com santo")
else:
    print ("Não começa com santo")

print (cidade[:5]=="santo")