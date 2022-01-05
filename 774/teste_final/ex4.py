# Crie a função triangulo(a,b,c) que classifica um triângulo como equilátero, isósceles ou 
# escaleno dados os comprimentos a, b, c dos três lados. Um triângulo é equilátero quando 
# tem os lados todos iguais, isósceles quando tem dois lados iguais e escaleno quando tem os 
# três lados diferentes

print ("\033[31;47m PROGRAMA TRIANGULO\033[m")
def fun_triangulo(a,b,c):

    if (a + b < c) or (a + c < b) or (b + c < a):
        print('\033[37;45m Nao é um triangulo \033[m')
    elif (a == b) and (a == c) :
        print('\033[37;45m Equilatero \033[m')
    elif (a==b) or (a==c) or (b==c):
        print('\033[37;45m Isósceles \033[m')
    else:
        print('\033[37;45m Escaleno \033[m')

fun_triangulo(float(input('Primeiro lado: ')) , float(input('Segundo  lado: ')) , float(input('Terceiro lado: ')))