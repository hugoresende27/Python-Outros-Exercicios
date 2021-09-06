def area(largura,comprimento):
    a=largura*comprimento
    print ("a área de um terreno %s por %s é de %s m2" %(largura,comprimento,a))

print ("Controle de Terrenos")
print ("-"*30)
#l=float(input("LARGURA (m): "))
#c=float(input("COMPRIMENTO (m): "))
area   (   float( input("LARGURA (m): ") )   ,   float( input("COMPRIMENTO (m): ") )   )