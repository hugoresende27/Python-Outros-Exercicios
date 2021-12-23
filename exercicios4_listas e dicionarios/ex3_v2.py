multiplos3=[]
pares=[]

for x in range(1,51):
    if x % 3 == 0:
        multiplos3.append(x)
print (multiplos3)

for x in multiplos3:
    if x % 2 == 0:
        pares.append(x)
print (pares)