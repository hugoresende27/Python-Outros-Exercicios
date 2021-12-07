#Programa que resolva o seguinte problema: Um comerciante comprou um produto e quer vendê lo 
# com lucro de 5€ se o valor da compra for menor que 20€; caso contrário, o lucro será de 10€. 
#O valor da compra é pedido pelo programa e é mostrado o valor da venda arredondado a uma 
#casa décimal. O valor de venda deve ficar, obrigatórimente, guardado numa variável.
#-pedir valor da compra
#se compra < 20 lucro = 5
#senao lucro = 10

compra = float(input("Qual o valor da compra? ->"))

if (compra<20):
    venda = compra+5
else:
    venda = compra +10
print("o valor da venda vai ser %.1f Euros"%venda)

