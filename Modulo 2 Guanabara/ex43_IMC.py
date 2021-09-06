from math import pow

print ("\033[7m=\033[m"*100)
print ("\033[7mPrograma IMC\033[m")

peso=float(input("Qual o seu peso em kg? --> "))
altura=float(input("Altura em metros (1.70m por exemplo)? --> "))

imc=peso/(pow(altura,2))

print ("\033[33mO seu IMC {:.2f} ".format(imc))

if imc<=18.5:
    print ("\033[31mAbaixo do peso\033[m")
elif 18.5<=imc<25:
    print ("\033[32mPeso ideal\033[m")
elif 25<=imc<30:
    print ("\033[34mSobrepeso\033[m")
elif 30<=imc<40:
    print ("\033[35mObesidade\033[m")
elif imc>=40:
    print ("\033[7;31mObesidade MORBIDA\033[m")
