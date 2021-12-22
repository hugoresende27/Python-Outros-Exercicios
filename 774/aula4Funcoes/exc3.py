#Crie uma função que receba como parâmetro uma lista com valores numéricos e retorne a 
#média desses valores.

def medias(x):
    return sum(x)/len(x)

valores = [11,14,15,17]

print ("Media: ",medias(valores))