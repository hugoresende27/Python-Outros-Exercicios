#Programa que simula uma calculadora. O programa pede ao utilizador dois valores e o caracter 
#com a operação que pretende realizar e devolve o resultado do cálculo.
while(True):
    op=input("Qual a operacao ( + | - | X | / | S(air)) --> ").upper()
    if (op[0]=='S'):exit()
    num1= float(input("VALOR 1--> "))
    num2= float(input("VALOR 2--> "))
    

    match op[0]:
        #case '+':print("SOMA: %.2f" %(num1+num2))
        case '+':print("SOMA: %s %s %s = %s" %(num1,op[0],num2,num1+num2))
        case '-':print("SOMA: %s %s %s = %s" %(num1,op[0],num2,num1-num2))
        case 'X':print("SOMA: %s %s %s = %s" %(num1,op[0],num2,num1*num2))
        case '/':print("SOMA: %s %s %s = %s" %(num1,op[0],num2,num1/num2))
        case 'S':exit()
        case _:print("Opcao inválida")
