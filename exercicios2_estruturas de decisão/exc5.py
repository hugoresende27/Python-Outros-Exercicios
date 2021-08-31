preco = float(input("qual o valor da compra? "))
if preco<20:
    valorfinal = preco + 5
else:
    valorfinal = preco + 10
print ("o preço inicial é %s e o valor final é %0.1f" %(preco,valorfinal))