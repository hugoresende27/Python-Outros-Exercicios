idade_mais_velho=0
f_menos20=[]
idades=[]

for x in range (1,5):
    nome=input("Nome pessoa {}--> ".format(x))
    idade=int(input("Idade pessoa {}--> ".format(x)))
    idades.append(idade)
    sexo=input("sexo pessoa (m/f) {}--> ".format(x)).lower()
    if ((sexo=="m") and (idade>idade_mais_velho)):
        m_mais_velho=nome
        idade_mais_velho=idade
    if((sexo=="f") and (idade<20)):
        f_menos20.append(idade)

print ("O homem mais velho {} tem {} anos".format(m_mais_velho,idade_mais_velho))
print ("Mulheres com menos de 20 anos {} no total de {}".format(f_menos20,len(f_menos20)))
print ("A media de idade de {} é {}".format(idades,(sum(idades)/4)))
