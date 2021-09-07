print ("\033[7m "+"{:=^40}".format("Programa palindromo")+"\033[m") 

frase=str(input("Digite uma frase:: ")).strip().upper()     #input frase strip tira espacos a mais e upper para MAIUSC
palavras=frase.split()              #cria uma lista, cada palavra um elemento
print (palavras)
junto=''.join(palavras)             #junta os elementos todos da lista palavras numa string sem espaços ''.join
print ("sem espaços ",junto)                   
inverso=""

for letra in range(len(junto)-1,-1,-1):     #ciclo comeca no ultimo elemento da string (len(junto)-1), vai até ao primeiro(-1)
    inverso+=junto[letra]                   #passo -1 para reverter, adciciona na var inverso as letras ao contrario, 1 a 1
print ("inverso ",inverso)   
if (inverso==junto):
    print ("TEMOS UM é palindromo")
else:
    print ("a frase NÂO É palindromo")