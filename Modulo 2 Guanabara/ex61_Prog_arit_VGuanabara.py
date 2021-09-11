print ("\033[32;7m "+"{:=^40}".format("10 PASSO DE Progressão Aritmética V_Guanabara")+"\033[m")

primeiro=int(input("Qual o primeiro termo? --> "))
razao=int(input("P.A.? --> "))
termo = primeiro
cont=1
while (cont<=10):
    print (" {} -> ".format(termo),end="")
    termo+=razao
    cont+=1
print ("\033[32;7mFIM...\033[m")

