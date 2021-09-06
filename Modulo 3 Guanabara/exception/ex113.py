def leiaInt(num):
    while True:
        try:
            n=int(input(num))    #try no input (int)
        except (ValueError,TypeError):                      
            print ("\033[1;31m -->Erro!! Digite um int válido!\033[0m")  #erro com print a vermelho 
            continue                        #se der erro, print e continue
        except (KeyboardInterrupt):
            print ("\033[1;31m Interrompido !!!!\033[0m")
            return 0                #se der ctrl + c interrompe o programa e mostra esta mensagem
        else:
            return n                        #se não der erro, return n


def leiaReal(num=0):
     while True:
        try:
            n=float(input(num))    
        except (ValueError,TypeError):                      
            print ("\033[1;31m -->Erro!! Digite um real válido!\033[0m")  #erro com print a vermelho  
            continue
        except (KeyboardInterrupt):
            print ("\033[1;31m Interrompido !!!!\033[0m")
            return 0    
        else:
            return n
       

i=leiaInt("digite um int:: ")
r=leiaReal("Digite um real:: ")
print ("O seu inteiro é %s e o real é %s" %(i,r))
print ('Hugo Resende @2021')