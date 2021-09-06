print ("\033[7m=\033[m"*100)
print ("\033[7mPrograma conversão\033[m")
n=int(input("Escreva um número inteiro para ser convertido--> "))

print ("\033[7m1.BINÁRIO\033[m")
print ("\033[7m2.OCTAL\033[m")
print ("\033[7m3.HEXADECIMAL\033[m")

op=int(input("Escolha a sua opção (1/2/3) --> "))
if op==1:
    print ("o número {} em binário fica {}".format(n,bin(n)[2:]))     #[2:] para nao imprimiro o0 sempre no principio
elif op==2:                                                           #vai dar print a partir do index 2, ignorando o 0 e1
    print ("o número {} em octal fica {}".format(n,oct(n)[2:])) 
elif op==3:
    print ("0 número {} em hexadecimal fica {}".format(n,hex(n)[2:]))
else:
    print ("Opção inválida")
