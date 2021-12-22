#Programa que imprime com o seguinte output a tabuada dum valor inserido pelo utilizador.

val = int(input("Qual a tabuada? --> "))
print 
for x in range (1,11,1):
    print ("\033[31m%s\033[m \033[32mX\033[m \033[33m%s\033[m = \033[34m%s\033[m "%(val,x,(x*val)))