print ("\033[31mOLÁ HUGO !!!")          #print letra vermelha
print ("\033[31;43m OLÈ!!!")            #print letra vermelha e fundo amarelo
print ("\033[1;31;43m OLÈEEE \033[m")   #print letra vermelha fundo amarelo negrito

print ("\033[4;30;45m OUTRA    \033[m")     #sublinhado cor letra 30 e de fundo 45


print ("\033[0;33;44m inversão \033[m")     #inversão entre o fundo e a cor da letra
print ("\033[7;33;44m inversão \033[m")  

a=5
b=7
print ("Os valores são \033[32m{}\033[m e \033[31m{}\033[m".format(a,b))      #\033[m para fechar \033[m

nome ="HUGO RESENDE"
print ("Prazer em conhecer te {}{}!!{} @@".format("\033[4;34m",nome,"\033[m"))      #dar print usando o format

cores={"limpa":"\033[m",
       "azul":"\033[34m",
       "amarelo":"\033[33m",
       "pretoebranco":"\033[7;30m"}

print ("TESTE CORES {}limpa {}amarelo aqui {}azul {}preto e branco".format(cores["limpa"],cores["amarelo"],cores["azul"],cores["pretoebranco"]))



