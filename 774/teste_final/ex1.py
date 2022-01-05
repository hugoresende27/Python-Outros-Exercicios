import math

print ("\033[37;42m PROGRAMA AREA CINZA\033[m")
lado=float(input("Qual o valor de L? :: "))
raio=lado/2
area_quadrado=lado*lado
area_circulo=math.pi*math.pow(raio,2)

area_sombreado=area_quadrado-area_circulo
print ("A área a sombreado tem %.2f" %area_sombreado)