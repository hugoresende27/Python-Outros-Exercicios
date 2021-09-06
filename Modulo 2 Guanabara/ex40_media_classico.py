print ("\033[7m=\033[m"*100)
print ("\033[7mPrograma NOTAS\033[m")

n1=float(input("nota 1--> "))
n2=float(input("nota 2--> "))

media=(n1+n2)/2
print ("\033[35mA sua média é {}\033[m".format(media))

if (media>9.5):
    print ("\033[32mAPROVADO")
elif (7<=media<9.5):
    print ("\033[33mRECUPERAÇÂO")
elif media<7:
    print ("\033[31mREPROVADO")