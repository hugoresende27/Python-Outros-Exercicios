
class Pessoa:
    def __init__(self,nome="",idade=0): #contruir o objeto
        self.nome=nome
        self.idade=idade
        
    def setNome(self,nome):
        self.nome = nome 
        
    def setIdade(self,idade):
        self.idade = idade 
        
    def getNome(self):
        return self.nome  
        
    def getIdade(self):
        return self.idade 
    
    def print1 (self):
        print ("Bem vindo %s com %d anos" %(self.nome,self.idade))
    

