

x="fanstastico"
print ("O python é " + x)

##################################################
valor1 = 5
valor2= 10
print (valor1+valor2)
print(valor1,valor2)
print (type(valor1))
print("O número é o %d e o outro %d" %(valor1,valor2))

#########################################################
numero = 10.9876
print ("int %d e dec %f" %(numero,numero))
print ("arredontado %2.2f"%numero)

###############################################################
txt1 = "o meu nome é {fname} e tenho{age}".format(fname="hugo", age=33)
print (txt1)

###############################################################
altura = 1.70
peso = 92
print(f"tenho {0:8>{altura}} de altura e {peso} Kgs")

################################################################
num1=0
while True:

    print("\n\t99 para sair")
    num1 = int(input("NUM1--> "))
    num2 = int(input("NUM2--> "))
    #comentário de código
    if (num1 == 99 or num2 == 99):
        break;
    elif num1>num2:
        print (num1," é maior do que ",num2)
    elif num2>num1:
        print (num2," é maior do que ",num1)
    elif num1==num2:
        print(num1," e ",num2," são iguais!")
        