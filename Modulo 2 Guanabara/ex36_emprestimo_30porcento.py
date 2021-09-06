print ("\033[7m=\033[m"*100)
print ("\033[33mPROGRAMA EMPRESTIMO BANCÁRIO 30%\033[m")

valor_casa=float(input("Valor total do Imóvel --> "))
sal=float(input("Qual o seu salário? --> "))
anos=int(input("Em quantos anos quer pagar? --> "))

meses=anos*12
pres=valor_casa/meses

print ("Vai ter um total de {} prestações, com o valor de {:.2f} mensal".format(meses,pres))

sal30=sal*0.30

if pres>sal30:
    print ("30% salário-->{}".format(sal30))
    print ("A sua prestação de {:.2f} excede 30% do seu salário, não podemos emprestar....".format(pres))
else:
    print ("30% salário-->{}".format(sal30))
    print ("A sua prestação de {:.2f} NÂO excede 30% do seu salário, TUDO OK".format(pres))


