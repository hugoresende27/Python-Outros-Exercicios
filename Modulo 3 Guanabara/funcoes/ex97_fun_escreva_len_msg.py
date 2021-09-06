import string

def escreva(msg):                   #minha solução, bem complexa, abaixo solução guanabara
    pos=0
    while pos<len(msg):
        print ("-",end="")
        pos+=1
    print ()
    print (msg)
    while pos>0:
        print ("-",end="")
        pos-=1
    print()

def escreva2(msg):                  #nesta solução, cria se a var tam e atribui-se o len de (msg)
    tam=len(msg)+4                  #a partir daí é fácil, -*tam
    print ("-"*tam)
    print ("  %s" %msg)
    print ("-"*tam)


escreva("Puta")
escreva ("Hugo")
escreva("CUrsão de python !!!")

escreva2("Muito mais fácil")
escreva2("Gustavo Guanas")