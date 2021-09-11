print ("\033[31;43m=="*10+"Programa Menu"+"=="*10+"\033[m")
num1=float(input("Valor 1--> "))
num2=float(input("Valor 2--> "))

opcao=0
while opcao!=5 or opcao!=4:


    print ("\033[31;43m=="*10+"MENU"+"=="*10)
    print ("[1]-SOMAR" )
    print ("[2]-MULTIPLICAR" )
    print ("[3]-MAIOR" )
    print ("[4]-NOVOS NUMEROS" )
    print ("[5]-SAIR"+"\033[m" )
    opcao=int(input("Opcao--> "))
    if opcao==1:
        print ("A soma de {} + {} é igual a {}".format(num1,num2,(num1+num2)))
        
    elif opcao==2:
        print ("A multiplicação de {} X {} é igual a {}".format(num1,num2,(num1*num2)))
        
    elif opcao==3:
        if num1>num2:
            print ("O maior entre  {} e {} é o {}".format(num1,num2,num1))
        elif num2>num1:
             print ("O maior entre  {} e {} é o {}".format(num1,num2,num2))
        else:
            print ("{} e {} são iguais ".format(num1,num2))
        

print ("FINAL DO PROGRAMA")
    


   