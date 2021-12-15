#Programa que imprime com o seguinte output a tabuada dum valor inserido pelo utilizador.

val = int(input("Qual a tabuada? --> "))
for x in range (1,11,1):
    print ("%s X %s = %s" %(val,x,(x*val)))