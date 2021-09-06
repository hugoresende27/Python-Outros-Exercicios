def aumentar (v,qtd,e=False):
    """
    -->função para aumentar um valor qtd%"""
    t=(v*qtd/100)+v
    if e:
        return moeda(t)
    else:
        return (t)

def diminuir (v,qtd,e=False):
    """
    -->função para diminuir um valor qtd%"""
    t=v-(v*qtd/100)
    if e:
        return moeda(t)
    else:
        return (t)

def dobro (v,e=False):
    if e:
        return moeda(v*2)
    else:
        return v
    
def metade (v,e=False):
    if e:
        return moeda(v/2,moeda="&")
    else:
        return v

def resumo(p,aum=0,red=0):
    """
    -->resumo das funçoes todas"""
    print ("-"*30)
    print ("\tRESUMO DO VALOR".center(30))
    print ("-"*30)
    print ("\tpreço analisado:: %s" %moeda(p))
    print ("\tdobro do preço:: %s" %dobro(p,True))
    print ("\tmetade do preço %s" %metade(p,True))
    print ("\t%s por cento de aumento %s" %(aum,aumentar(p,aum,True)))
    print ("\t%s por cento de redução %s" %(red,diminuir(p,red,True)))
    print ("-"*30)

def moeda(x,moeda="€"):
    """
    -->função para adicionar 
    o simbolo do € euro e trocar
    os . por ,"""
    return ("-->%8.2f %s" %(x,moeda)).replace(".",",")          




