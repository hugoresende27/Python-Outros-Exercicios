print ("\033[33;7m "+"{:=^40}".format("Programa soma valores 999 V2")+"\033[m")
contador=soma=0
while True:
    n = int(input("VALOR:: "))
    if n==999:
        break
    soma+=n
    contador+=1

print (f"a soma é {soma} no total de {contador} valores")