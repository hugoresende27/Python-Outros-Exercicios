print ("\033[7m "+"{:=^40}".format("Programa PARES 1 a 50")+"\033[m")

for x in range (1,51):
    if x%2==0:
        print ("Este é par --> {}".format(x))
        