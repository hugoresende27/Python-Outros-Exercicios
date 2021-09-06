matriz=[[0,0,0],[0,0,0],[0,0,0]]            #iniciar lista com 3 sublistas e 3 elementos a 0 dentro de cada sublista
somapares=maior=somacoluna3=0               #iniciar var 

for linha in range (3):                     #para 3 linhas
    for coluna in range (3):                #dentro de 3 colunas
        matriz[linha][coluna] = int(input("Valor [%s,%s] :: " %(linha,coluna))) #input valor com coordenadas

print("&"*50)
for linha in range (3):                     #para linha até 3
    for coluna in range (3):                #até 3 colunas, 
        print ("[%s]" %matriz[linha][coluna],end=" ")   #print da matriz com [] elemento a elemento tudo seguido, end=""
        if matriz[linha][coluna] %2 ==0:                #se o valor da matriz for par
            somapares+=matriz[linha][coluna]            #adiciona a somapares
    print()                                             #quando chegar à coluna 3, quebra a linha com o print()

print ("A soma dos pares é :: %s" %somapares) 
for linha in range(0,3):                                #percorre a linhas                  ??
    somacoluna3+=matriz[linha][2]                       #soma o valor da [2] de cada linha
print ("A soma dos valores da coluna 3 é %s" %somacoluna3)

for coluna in range (3):                                #percorre de 0 a 3
    if coluna == 0:                                     #no primeiro ciclo, maior = elemento [0] da linha [1]
        maior=matriz[1][coluna]
    elif matriz[1][coluna]>maior:                      #depois do primeiro ciclo, se elemento maior assume valor 
        maior=matriz[1][coluna]
print ("O maior valor da segunda linha é %s" %maior)
    


