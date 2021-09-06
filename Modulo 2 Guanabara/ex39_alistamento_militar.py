from datetime import date
ano_a=date.today().year

print ("\033[7m=\033[m"*100)
print ("\033[7mPrograma ALISTAMEnTO\033[m")

ano_n=int(input ("Ano nascimento--> "))
idade=ano_a-ano_n

print ("Tens {} anos...".format(idade))

if idade>18:
    anos=idade-18
    print ("Já passou da idade {} anos".format(anos))
    print ("Deveria ter se alistado em {}".format(ano_a-anos))
elif idade<18:
    print ("Ainda falta {} anos ".format(18-idade))
    print ("Deve alistar se em {}".format(ano_a+(18-idade)))
else:
    print ("Este ano tem de se alistar")