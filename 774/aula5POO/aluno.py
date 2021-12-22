from pessoa import Pessoa

class Aluno(Pessoa):#classe filha de (Pessoa)
    def __init__(self,nome,idade,turma):
        super().__init__(nome,idade) #super() para aceder aos metodos e atributos do pai
        self.turma=turma
    
    def setturma(self,turma):
        self.turma=turma
    def getturma(self):
        return self.turma
    
    def print1 (self):
        print ("Bem vindo %s com %d anos  da turma  %s" %(self.nome,self.idade,self.turma))
