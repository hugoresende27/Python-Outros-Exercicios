try:
    a=int(input("valor int a::"))                   #operação
    b=int(input('valor int b::'))
    r=a/b
except Exception as erro:                                       #para identificar o tipo de exepção
    print('o seu valor falhou porque %s' %erro.__class__)       #falhou     
else:
    print ('o seu valor é %s' %r)                   #deu certo
finally:                                            #executa sempre, dando certo ou errado
    print ('Hugo Resende @2021')                    #falhou/deu certo

#################################

try:
    num1=int(input('valor 1: '))
    num2=int(input('valor 2:: '))
    tot=num1/num2
except (ValueError,TypeError):                      
    print ('problema de valor ou digitação')
except ZeroDivisionError:
    print ('não pode dividir por zero')
except KeyboardInterrupt:
    print ('não introduziu nada')
except Exception as x:
    print ("o erro encontrado foi " , x.__cause__)
else:
    print ('o resultado de %s / %s = %s' %(num1,num2,tot))
finally:
    print ('volte sempre, obrigado...')