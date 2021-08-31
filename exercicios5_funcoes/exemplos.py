#########
def minha_funcao():
    print ("Função Activada !!!")

def minha_funcao2(fname):
    print ("NOME :: "+fname)

def minha_funcao3(*kids):       #argumentos arbitrários, não sei quantos entram *
    print ("Elemento da terceira posição ::", kids[2])

def minha_funcao4 (pais="Brasil"):      #argumentos padrão
    print ("Eu sou de "+pais)

def minha_funcao5(comida):
    for x in comida:
        print (x)

def minha_funcao6(x):
    return 5*x


fruta=["Uva","Banana","Maça"]
global total 
total=10


#Inicio programa 
res =" "
while res !="s" or res!= "n":
    print ("O programa começa aqui! ")
    res=input("Quer iniciar a função? ").lower()
    if res == "s":
        minha_funcao() 
        minha_funcao2("Hugo") 
        minha_funcao3("Hugo", 365, "Outro", "Qualquer") 
        minha_funcao4("Portugal")
        minha_funcao4() 
        minha_funcao5(fruta)
        print( minha_funcao6(3))
        print( minha_funcao6(5))
        print( minha_funcao6(10)) #chamada da função
        import math

        print (math.pi)
    
    elif res =="n":
        exit()
    else:
        print("opcao inválida")


