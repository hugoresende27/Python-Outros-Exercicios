def voto(ano):
    """programa q com input de ano diz a idade 
    do eleitor e se o eleitor tem voto OPCIONAL, NÃO VOTA
    ou OBRIGATÓRIO"""
    
    from datetime import datetime                   #importei dentro da classe, economiza muita memória
    currentYear = datetime.now().year

    idade=currentYear-ano
    if idade>=65 or 18>idade >= 16:  
        return ("O eleitor tem %s anos::: OPCIONAL" %idade)
    elif idade<18:
        return ("O eleitor tem %s anos:::NÃO VOTA"%idade)
    else:
        return ("O eleitor tem %s anos:::VOTO OBRIGATÓRIO"%idade)


nasc=int(input("Ano de Nascimento:: "))
print (voto(nasc))
print(voto(2010))