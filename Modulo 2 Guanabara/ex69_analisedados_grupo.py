print ("\033[7m "+"{:=^40}".format("ANALISE DE DADOS")+"\033[m")

pessoas_18=0
homens=0
mulheres20=0
while True:
    idade=int(input("\033[33;7mIdade: \033[m"))
    if idade>=18:
        pessoas_18+=1

    sexo= " "
    while not sexo in 'mf':
        sexo=str(input("\033[33;7mSexo: [M/F]: \033[m")).strip().lower()[0]
        
    if sexo=="m":
        homens+=1   
    elif idade<=20 and sexo=="f":
        mulheres20+=1
   
    sair = " "
    while not sair in 'sn':
        sair=str(input("Quer continuar? [S/N]--> ")).strip().lower()[0]
    if sair=="n":
        break

print (f"Total de pessoas com mais de 18 anos: {pessoas_18}")  
print (f"Ao todo temos {homens} homens registados")
print (f"{mulheres20} mulheres com menos de 20 anos") 



print ("\033[31;7mFINALIZANDO....\033[m")