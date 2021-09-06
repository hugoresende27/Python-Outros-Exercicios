from math import sin,cos,tan,radians

a=int(input("Quantos ° graus tem o angulo? --> "))
print ("O cosseno é {:.2f}".format(cos(radians(a))))
print ("O seno é {:.2f}".format(sin(radians(a))))
print("A tangente é {:.2f}".format(tan(radians(a))))