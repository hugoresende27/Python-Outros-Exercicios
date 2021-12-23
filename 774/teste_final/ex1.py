import math

lado=float(input("Qual o valor de L? :: "))
raio=lado/2
area_quadrado=lado*lado
area_circulo=math.pi*raio*raio

area_sombreado=area_quadrado-area_circulo
print ("A área a sombreado tem %.2f" %area_sombreado)