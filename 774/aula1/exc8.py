#Programa que simula uma calculadora. O programa pede ao utilizador dois valores e o caracter 
#com a operação que pretende realizar e devolve o resultado do cálculo.

num1= float(input("VALOR 1--> "))
num2= float(input("VALOR 2--> "))
op=input("Qual a operacao ( + | - | X | / ) --> ").upper()
match op:
    case '+':print("SOMA: %.2f" %(num1+num2))
    case '-':print("SUB: %.2f" %(num1-num2))
    case 'X':print("MULT: %.2f" %(num1*num2))
    case '/':print("DIV: %.2f" %(num1/num2))
    case _:print("Opcao inválida")