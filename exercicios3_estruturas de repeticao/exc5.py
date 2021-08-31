tamanho = int(input("Qual o tamanho do quadrado?"))

for x in range (tamanho):
    for y in range (tamanho):
        print ("$", end =" ")
    print ("")

n = int(input("Digite um número: "))
for x in range (n):
    print ('*'*n)

#introduzir o numero de linhas e colunas
line = int(input('Introduza número de linhas: '))
column = int(input('Introduza o número de colunas: '))

#desenhar forma
for x in range(line):
    simbol  = ''
    for y in range(column):
        simbol +='* '
    print(simbol)

