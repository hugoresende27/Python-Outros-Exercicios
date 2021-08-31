class Caderno():
    def __init__(self,cor,np):
        print ("Caderno Iniciado")
        self.cor=cor
        self.np=np

    def getCor(self):               #os gets permitem o retorno do valor dos atributos para o programa 
        return self.cor

    def getNp(self):                
        return self.np              

    def setCor(self,cor):
        self.cor=cor                #os sets permitem atribuir/modificar o valor dos atributos

    def setNp(self,np):
        self.np=np  
c1=Caderno("amarelo", 50)
print (c1.cor)      #não é a melhor pratica de acesso aos atributos
c2=Caderno("Azul",69)
print (c2.getCor())
c2.setCor("Preto")
print (c2.getCor())

