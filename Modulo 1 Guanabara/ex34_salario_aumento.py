

sal=float(input("Qual o seu salário? --> "))
if (sal>1250):
    novosal=sal+(sal*0.10)
    print ("O teu salário era {} euros com 10% de aumento fica {} euros".format(sal,novosal))
else:
    novosal=sal+(sal*0.15)
    print ("O teu salário era {} euros com 15% de aumento fica {} euros".format(sal,novosal))