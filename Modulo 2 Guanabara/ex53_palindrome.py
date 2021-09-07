print ("\033[7m "+"{:=^40}".format("Programa palindromo")+"\033[m") 

frase=input("Escreva a frase--> ").replace(" ","")  #subs espaços em braco " " por ""(sem espaço)
print ("frase sem espaços ---> {:<10}  ".format( frase))
frase2=frase[::-1]              #inverter uma string
print ("frase sem espaços invertida ---> {}".format( frase2))
if (frase==frase2):        #usar o slice [start:end:step], -1 reverse a string, se sim é palindromo
    print ("é palindromo")
else:
    print ("NÂO É")