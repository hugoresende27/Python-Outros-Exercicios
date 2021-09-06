expressao = str(input("digite uma expressão :: "))
pilha=[]
posicao=0
for index,x in enumerate (expressao):             #percorrer a expressao
    if x == "(":                #se encontrar o parenteses a abri 
        pilha.append("(")       #coloco na pilha vazia

    elif x == ")":              #se encontrar o parenteses a fechar
        if len(pilha)>0:        #se a pilha tiver um elemento, ou seja >0, ou seja tiver um parenteses aberto
            pilha.pop()         #remove ultimo elemento da pilha, ou seja vai esvaziar a pilha
        else:
            pilha.append(")")   #se não tiver nenhum elemento na pilha, vai ficar o parenteses por fechar 
            posicao=index
            break               #ficando assim um elemento na pilha, depois faz o break

if len(pilha) == 0:             #então, se a pilha não tiver elementos tudo ok
    print ("a expressão %s está certa !" %expressao)
if len(pilha)>0:                #se a pilha tiver um elemento, print do elemento q está a mais "(" ou ")"
    print ("a expressão %s NÃO está certa !, tem isto a mais %s na posicao %s" %(expressao,pilha,posicao))