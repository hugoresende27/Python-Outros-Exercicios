lar= float(input("Qual a largura da parede? "))
alt = float(input("Qual a altura da parede? "))
area = lar * alt
print ("A sua parede tem dimensão de {} X {} a área é {:.2f}m² e precisa de {:.1f}L de tinta".format(lar,alt,area,(area/2)))