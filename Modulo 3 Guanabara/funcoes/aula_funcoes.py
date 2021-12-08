def lin():
    print ("-"*30)

def mensagem(msg):                  #funcao com parametros, neste caso msg.
    print ("-"*30)
    print (msg)                     #print do parametro
    print ("-"*30)
  
#programa principal
lin()
mensagem ("APRENDA PYTHON")
mensagem ("HUGO RESENDE")
##########################################
def soma(a,b):          
    return (a+b)

def sub(a,b):
    print (a-b)


#Guanabara fala para deixar 2 linhas entre def's e programa principal ?!
print (soma(4,4))       
print (soma(b=20,a=12))     #posso passar parametros definindo qual o a e qual o b
sub(20,5)
sub(b=20,a=5)

#######################################  desampacotamento tupla
def contador (*num):
    print (num)             #cria uma tupla com todos os valores
    for valor in num:
        print (valor,end="..")
    print ("FIM")
    print ("len",len(num))


contador (2,1,7)
contador (8,0)
contador (4,4,7,6,2)
