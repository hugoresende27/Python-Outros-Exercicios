#Crie uma função que recebe como argumentos dois valores numéricos e escreva para o ecrã o maior

def maior (a,b):
    if (a>b):return a
    else: return b
    
def maior2 (a,b):
    return max(a,b)
    
a=float(input("VALOR A:: "))
b=float(input("VALOR B:: "))

print ("MAIOR É O ",maior(a,b))
print ("MAIOR É O ",maior2(a,b))