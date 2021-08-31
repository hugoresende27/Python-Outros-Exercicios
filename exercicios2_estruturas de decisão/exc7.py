escolha = input("qual a operação? | + | - | * | / | ---->> ")

a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))


if escolha=='+':
    print ("%.2f + %.2f = %.2f "%(a,b,a+b))
elif escolha=='-':
     print ("%.2f - %.2f = %.2f "%(a,b,a-b))
elif escolha=='*':
     print ("%.2f X %.2f = %.2f "%(a,b,a*b))
elif escolha=='/':
    if (b!=0):
        print ("%.2f : %.2f = %.2f "%(a,b,a/b))
    else:
        print ("Não podes dividir por zero!!")
else:
    print ("Escolha inválida")