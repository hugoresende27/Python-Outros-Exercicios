lista=[]

for x in range (5):
    valor=int(input("Digite um valor:: "))
    if x == 0 or valor>lista[-1]:               #se a posição do index for 0 ou o valor for > do q o ultimo elemento 
        lista.append(valor)                     #append no final da lista
        print("adicionado ao final da lista")
    else:
        posicao=0                               #contador posicao
        while posicao<len(lista):               #enquanto a posicao for menor do q a ultima posicao da lista
            if valor<=lista[posicao]:           #verifica em cada index/posicao se o valor a inserir é <= ao valor de
                lista.insert(posicao,valor)     #index, se for insere no index/posicao o valor/elemento
                print("Inseriu o valor %s na posicao %s" %(valor,posicao))
                break                           #quebrar o ciclo while
            posicao+=1                          #adiciona +1 à posicao 


#lista.sort()
print ("Os valores digitados em ordem foram %s" %lista)

