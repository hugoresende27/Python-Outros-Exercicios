print ("\033[7m "+"{:=^40}".format("Programa Tabuadas V2")+"\033[m")
n=int(input("Tabuada do ::: "))
for x in range (1,11):
    print ("\033[31;43m{} X {:2} = {}\033[m".format(n,x,(n*x)))  #{:2} para ficarem os espaços certos, 
                                                                 #{:2} termina sempre na pos 2