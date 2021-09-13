print ("\033[31;7m "+"{:=^40}".format("BANCO HR V2")+"\033[m")
quantia=float(input("Qual a quantia? --> "))

notas=quantia//50                           #parte inteira da divisão, por exemplo 75 // 50 = 1
print (f"Existem {notas:.0f} notas de 50€")
quantia= quantia-(notas*50)                 #quantia vai receber, por exemplo 75-(1*50) = 25
                                            #assim obtemos o q resta da quantia depois de tirarmos as notas de 50 
notas=quantia//20                           #parte inteira da divisao, por exemplo 25 // 20 = 1
print (f"Existem {notas:.0f} notas de 20€")
quantia= quantia-(notas*20)                 #25-(1*20) = 5, sobram 5 euros

notas=quantia//10                           #mesmo principio para quantas notas notas e moedas de 1 euro q eu quiser
print (f"Existem {notas:.0f} notas de 10€")
quantia= quantia-(notas*10)

notas=quantia//5
print (f"Existem {notas:.0f} notas de 5€")
quantia= quantia-(notas*5)

notas=quantia//1
print (f"Existem {notas:.0f} moedas de 1€")
quantia= quantia-(notas*1)

notas=quantia//0.5
print (f"Existem {notas:.0f} moedas de 0.50€")
quantia= quantia-(notas*0.5)

notas=quantia//0.2
print (f"Existem {notas:.0f} moedas de 0.20€")
quantia= quantia-(notas*0.2)

notas=quantia//0.1
print (f"Existem {notas:.0f} moedas de 0.10€")
quantia= quantia-(notas*0.1)

notas=quantia//0.05
print (f"Existem {notas:.0f} moedas de 0.05€")
quantia= quantia-(notas*0.05)


print ("\033[31;7mFIM...\033[m")



