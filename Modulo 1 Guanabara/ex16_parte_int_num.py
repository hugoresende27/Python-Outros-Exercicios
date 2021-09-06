#import math
from math import trunc

n = float(input("Qual o número?? --> "))
#print ("O número {} tem parte interia {} .".format(n,(math.trunc(n))))
print ("O número {} tem parte interia {} .".format(n,(trunc(n))))
print ("Outra maneira seria, mas vai arredondar para cima {:.0f}".format(n))
print ("outra seria int(n) {}".format(int(n)))
