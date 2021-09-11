print ("\033[32;7m "+"{:=^40}".format("10 PASSO DE Progressão Aritmética V_Guanabara")+"\033[m")

primeiro=int(input("Qual o primeiro termo? --> "))
razao=int(input("P.A.? --> "))
termo = primeiro
cont=1
total=0
mais=10
while mais !=0:
    total+=mais
    while (cont<=total):
        print (" {} -> ".format(termo),end="")
        termo+=razao
        cont+=1
    print ("\033[32;7mPAUSA...\033[m")
    mais=int(input("Quantos termos mais?? (0 para sair) -> "))
print ("Progressão finalizada com {} termos mostrados".format(total))
print ("\033[32;7mFIM...\033[m")