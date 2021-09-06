#print ("\033[7m=\033[m"*100)
print ("\033[7m "+"{:=^40}".format("Programa PAGAMENTOS")+"\033[m")

preco=float(input("Qual o preço do produto--> "))
print ("""Qual a modalidade de pagamento::
        [1].Dinheiro/Cheque:10% desconto
        [2].Cartão:5% desconto
        [3].duas x em cartão
        [4].três x ou mais:20% juros""")

op=int(input("\033[7mOpção-->\033[m"))
if op==1:
    total=preco-(preco*10)
    print ("Vai pagar um total de {}".format(preco-(preco*0.10)))
elif op==2:
    total=preco-(preco*0.05)
    print ("Vai pagar um total de {}".format(preco-(preco*0.05)))
elif op==3:
    total=preco
    print ("Vai pagar {} euros em 2 prestações de {} euros".format(preco,(preco/2)))
elif op==4:
    total=preco+(preco*0.20)
    pres=int(input("Quantas prestações? --> "))
    custo=total/pres
    
    print ("vai pagar ao todo {}€ em {} prestações, cada uma no valor de {:.2f}€".format(total,pres,custo))
else:
    total=0
    print("Opção errada")

print ("Sua compra de {} euros vai custar o total de {} euros".format(preco,total))