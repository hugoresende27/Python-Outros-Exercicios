nome =input("Qual o nome?? ")
print ("O seu nome é {:20} !!" .format(nome))       #ocupa 20 carateres
print ("O seu nome é {:<20} !!" .format(nome))      #alinhado à esquerda
print ("O seu nome é {:>20} !!" .format(nome))      #alinhado à direita
print ("O seu nome é {:^20} !!" .format(nome))      #alinhado ao centro
print ("O seu nome é {:=^20} !!" .format(nome))      #alinhado ao centro e o resto com =