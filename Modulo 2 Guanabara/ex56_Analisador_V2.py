somaidade=0
mediaidade=0
maioridadehomem=0
nomemaisvelho=""
totmulher20=0

for p in range(1,5):
    print ("PESSOA {}".format(p))
    nome=str(input("NOME::: ")).strip()
    idade=int(input("IDADE:: "))
    sexo =str(input("SEXO (M/F):: ")).strip()
    somaidade+=idade
    if p==1 and sexo in 'Mm':       #na primeira iteracao, se o sexo for M ou m
        maioridadehomem=idade       #a idade recebida é a idade do homem + velho
        nomemaisvelho=nome          #o nome recebido é o nome do homem + velho 
    if sexo in 'Mm' and idade>maioridadehomem:  #se o sexo for M ou m e a idade for maior do que a idade do homem+velho
        maioridadehomem=idade
        nomemaisvelho=nome
    if sexo in 'Ff' and idade<20:       #se o sexo for F ou f e a idade inferior a 20
        totmulher20+=1                  #adiciona +1 à var totmulher20


mediaidade=somaidade/4

print ("A media do grupo é {}".format(mediaidade))
print ("O Homem mais velho tem {} anos e tem o nome {}".format(maioridadehomem,nomemaisvelho))
print ("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))