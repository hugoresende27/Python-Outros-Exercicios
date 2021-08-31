x=1
pares=impares=0


while x<=5:
   num = float(input("Introduza %sº valor:: "%x))
   x+=1
   if num % 2 == 0:pares+=1
   else:impares+=1
print ("Existem %s numeros pares e %s numeros impares"%(pares,impares))


pares2=impares2=0


for y in range (5):
    num2 = float(input("Introduza %sº valor:: "%(y+1)))
    if num2 % 2 == 0:pares2+=1
    else:impares2+=1
print ("Existem %s numeros pares e %s numeros impares"%(pares2,impares2))

