n = int(input("Qual o valor?? (0-9999) -->"))

print ("Analisando o número {}".format(n))
u= n // 1 % 10          #divide por 1 e depois o resto da divisão por 10, obtenho a unidade
d= n // 10 % 10            #divide por 10 e depois o resto da divisão por 10, obtenho as dezenas
c= n // 100 % 10       #número divido por 100, pega os 2 primeiros numeros, resto da divisão por 10
m= n // 1000 % 10

print ("Milhar ---> {}".format(m))
print ("Centena ---> {}".format(c))
print ("Dezena ---> {}".format(d))
print ("Unidade ---> {}".format(u))


