from datetime import date

ano = date.today().year
print ("\033[7m=\033[m"*100)
print ("\033[7mPrograma NATAÇÃO\033[m")
ano_n=int(input("Ano de nascimento--> "))
idade=ano-ano_n

print ("\033[7mTens {} anos de idade\033[m".format(idade))
if(idade<=9):
    print ("MIRIM")
elif (idade<=14):
    print ("INFANTIL")
elif (idade<=19):
    print ("JUNIOR")
elif (idade<=20):
    print ("SENIOR")
elif (idade>20):                #else: print("MASTER")
    print ("MASTER")