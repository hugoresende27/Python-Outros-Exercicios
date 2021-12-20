frutas = ['Maça', 'Pêra','Kiwi','Uva','banana','Papaia']

for x in frutas:
    print (x)                       #IMPRIME TODOS OS ELEMENTOS DA LISTA
print("************************")
[print(x) for x in frutas]          #ENTRE [] TBM IMPRIME TODOS OS ELEMENTOS DA LISTA
print("************************")
for i in range(len(frutas)):        #COM O len() TENHO O NÚMERO DOS INDEXES
    print(frutas[i],"-->",i)
print("************************")
frutas.sort()                       #ORDENAR A LISTA COM sort(), atenção Python ordena primeiro as Maiúsculas
print (frutas)
print("************************")
frutas.sort(key=str.lower)          #USAR key=str.lower TRANSFORMA TODAS AS OCORRÊNCIAS a minusculas e depois ordena
print (frutas)
print("************************")
frutas.sort(reverse = False)       #REVERSE PODE SER TRUE OU FALSE, ORDENAR LISTA
print(frutas)

