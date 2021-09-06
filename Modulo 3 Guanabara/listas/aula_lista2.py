teste=list()
teste.append("Hugo")
teste.append(32)
galera=list()
galera.append(teste[:])         #[:] é para fazer a cópia da lista, e nao substituir os elementos mas sim adicionar
teste[0]="Maria"
teste[1]=40
print ("::::::::::::::",teste)
galera.append(teste[:])         #[:] se não usar isto, as listas ficam ligadas e tudo o q ocorre numa ocorre na outra
print (galera)

galera2=[["joao",11],["hugo",32],["jose",55],["toto",68]]
print (galera2[2][1])       #primeiro a posicao da sublista [] e depois o elemento []

for p in galera2:
    print ("%s tem %s anos de idade" %(p[0],p[1]))      #print dos elementos da sublista [0] e depois
                                                        #dos seus elementos [1] com texto pelo meio

