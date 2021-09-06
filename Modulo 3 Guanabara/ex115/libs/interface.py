
from time import sleep
from uteis import dados,formatacoes

def menu():

    
    formatacoes.linha()
    formatacoes.cabecalho("SISTEMA DE ARQUIVO 1.0")
    formatacoes.linha()
    formatacoes.cabecalho("MENU PRINCIPAL")
    print ("1-> Consultar Pessoas")
    print ("2-> Registar Pessoas")
    print ("3-> Sair")
    while True:
        op=dados.leiaInt("Sua opção--> ")
        if op==1:
            consultar()
        elif op==2:
            registar()
        elif op==3:
            print ("Saindo do sistema....Hugo Resende @2021")
            exit()
        else:
            print ("Opção Inválida!")
        
def consultar():
    print ("consulta")
    sleep (0.5)
    try:
        f= open("pessoas.txt" , "r")  #r read  
    except IOError:
        f= open("pessoas.txt" , "w") #write, create if not exist
    else:
        f= open("pessoas.txt" , "r")
        print (f.read())

    menu()

def registar():
    print ("regista")
    f=open("pessoas.txt" , "a")     #append
    pessoas={}
    pessoas["nome"]=str(input("NOME::: "))
    f.write("\n%s" %pessoas["nome"])
    pessoas["idade"]=dados.leiaInt("IDADE::: ")

    tam_nome=len(pessoas["nome"])
    f.write(" "*(25-tam_nome)+str(pessoas["idade"]))
   
        
    f.close()
    print ("Registo de %s adicionado" %pessoas["nome"])
    sleep (0.5)

    menu()
