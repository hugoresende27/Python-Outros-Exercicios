print ("\033[7m=\033[m"*100)
print ("\033[7mPrograma TRIÂNGULO\033[m")

r1=float(input("Primeira reta--> "))
r2=float(input("Segunda reta--> "))
r3=float(input("Terceira reta--> "))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print (" É triângulo")
    if (r1==r2==r3):
        print ("Triângulo Equilátero")
    #elif (r1==r2 or r2==r3 or r3==r1):
    #    print ("Triângulo Isóceles")
    #else:
    #    print ("Triângulo Escaleno")
    elif (r1!=r2!=r3!=r1):      #outra maneira, se os lados todos != escaleno e else para isóceles
        print ("ESCALENO")
    else:
        print ("ISÓCELES")

else:
    print ("NÂO É triângulo")