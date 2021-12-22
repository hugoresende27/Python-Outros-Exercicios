def soma(x,y):
    global total #global total cria associa total a total do global
    total = x+y
    print ("TOTAL:: ", total)
    
total= 10
soma(3,5)
print ("O total principal, ",total)
