from pessoa import Pessoa

class Professor(Pessoa):#classe filha de (Pessoa)
    def __init__(self,nome,idade,disciplina):
        super().__init__(nome,idade) #super() para aceder aos metodos e atributos do pai
        self.disciplina=disciplina
    
    def setdisciplina(self,disciplina):
        self.disciplina=disciplina
    def getdisciplina(self):
        return self.disciplina
    
    def print1 (self):
        print ("Bem vindo %s com %d anos lecciona a disciplina de %s" %(self.nome,self.idade,self.disciplina))
