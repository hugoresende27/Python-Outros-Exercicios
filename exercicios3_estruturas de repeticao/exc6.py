x=1
soma=0
soma2=0
while x<=5:
   num = float(input("Introduza %sº valor:: "%x))
   x+=1
   if num>0:soma+=num
      
print ("A soma dos positivos",soma)

for y in range (5):
    num2 = float(input("Introduza %sº valor:: "%(y+1))) 
    if num2>0:soma2+=num2
print ("A soma dos positivos",soma2)
