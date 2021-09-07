print ("\033[7m "+"{:=^40}".format("Programa palindromo")+"\033[m") 

frase=input("Escreva a frase--> ").replace(" ","")  #subs espaços em braco " " por ""(sem espaço)
print (frase)
if (frase==frase[::-1]):        #usar o slice [start:end:step], -1 reverse a string, se sim é palindromo
    print ("é palindromo")
else:
    print ("NÂO É")