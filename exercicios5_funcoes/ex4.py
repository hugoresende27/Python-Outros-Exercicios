def media (valores):
    return sum(valores)/len(valores)


def media_lista(valores):
    soma=0
    for valor in valores:
        soma = soma + valor
    return soma/len(valores)

############
valores = {12,33,44,46,33,20}

print (media(valores))
print (media_lista(valores))