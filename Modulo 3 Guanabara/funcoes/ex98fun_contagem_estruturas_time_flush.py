from time import sleep

def contador (inicio,fim,passo):
    print ("Contagem de %s até %s de %s em %s" %(inicio,fim,passo,passo))
    if passo<0:
        passo *= -1 #ou  passo=abs(passo)            passo é sempre positivo
    if passo==0:                                #tinha estas condições fora da def, aqui ficam melhor
        passo=1
    if inicio<fim:
        while inicio<=fim:          
            print (inicio,end=" ", flush=True )         #para a função time preciso do Flush=True,
            #sleep(0.5)                                  #depois da actualização, antes funcionava
            inicio+=passo       
        print ("FIM")
    else:
        while inicio>=fim:
            print (inicio, end=" ", flush=True  )
            #sleep(0.5)
            inicio-=passo      
        print ("FIM")



contador (1,10,1)
contador (inicio=10,fim=0,passo=2)
print ("Personaliza a contagem!")
i=int(input("Inicio:: "))
f=int(input("Fim:: "))
p=int(input("Passo:: "))
contador(i,f,p)