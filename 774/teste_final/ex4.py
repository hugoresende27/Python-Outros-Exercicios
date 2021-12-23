

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