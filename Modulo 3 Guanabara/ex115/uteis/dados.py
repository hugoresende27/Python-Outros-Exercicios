def leiaInt(num=0):
     while True:
        try:
            n=int(input(num))    
        except (ValueError,TypeError):                      
            print ("\033[1;31m -->Erro!! Digite opção 1/2/3 !\033[0m")  #erro com print a vermelho  
            continue
        except (KeyboardInterrupt):
            print ("\033[1;31m Interrompido !!!!\033[0m")
            exit()   
        else:
            return n