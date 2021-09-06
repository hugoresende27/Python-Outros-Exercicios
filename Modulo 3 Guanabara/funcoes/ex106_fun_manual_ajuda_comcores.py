c=("\033[m",                #sem cor        [0]             #var GLOBAL pode ser usada no programa inteiro
   "\033[0;30;41m",         #[1] vermelho
   "\033[0;30;42m",         #[2] verde
   "\033[0;30;43m",         #[3] amarelo
   "\033[0;30;44m",         #[4] azul
   "\033[0;30;45m",)        #[5] roxo


def ajuda(com):
    """-->função ajuda, escreva uma função e veja o help
    do manual"""

    titulo("ACESSANDO AO MANUAL %s" %com,4)     #uso da funcao titulo
    print (c[5],end="")
    help(com)
    print (c[0],end="")

def titulo(msg,cor=0):
    """-->Função titulo, recebe a mensagem no parametro 1 
    recebe o codigo da cor no parametro 2, por defeito 0
    1:vermelho;2:verde;3:amarelo;4:azul;5:roxo;0:semcor"""

    tam =len(msg)+4             #para fazer a linha, leio o tamanho da msg e adiciono 4 valores
    print (c[cor],end="")       #print da lista cor, na posição de input [cor], end seguido
    print ("="*tam)             #print da linha
    print ("  %s"%msg)      
    print ("="*tam)
    print (c[0],end="")         #para voltar a tirar a cor, print da lista na posição [0]=semcor



comando=""
while True:
    titulo("PYTHON HELP Hugo Resende@2021",2)
    comando=str(input("Função ou Biblioteca:: "))
    if comando.upper()=="FIM":
        break
    else:
        ajuda(comando)
titulo("ADEUS",1)

    
