def iterate (lista,start,end):
    if start < 0 or end >= len(lista) or start > end:
        return
    print (lista[start])
    
    iterate(lista,start + 1, end)
    


l = [2,5,6,9,5,22,1,4,7,8]
s = 0
e = 10
iterate(l,s,e)