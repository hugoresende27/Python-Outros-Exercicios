class Pessoa:
    def __init__(self,nome="",idade=0):
        self.nome=nome
        self.idade=idade

    def mostraNome(self):
        print ("Olá o meu nome é "+self.nome)

class Estudante(Pessoa):
    def __init__ (self,nome,idade,ano):
     #   Pessoa.__init__(self,nome="",idade=0)           #self.nome=nome
        super().__init__(nome,idade)                     #self.idade=idade  igual ao de cima
        self.ano=ano    

    def bemVindo(self):
        print ("Bem vindo,",self.nome,"no ano ", self.ano)

e1=Estudante("Hugo",32,3)
print (e1.nome,e1.idade,e1.ano)
e1.bemVindo()
e1.mostraNome()

p1=Pessoa("Rui",30)
p1.mostraNome()
#p1.bemVindo()              nao posso chamar fora da classe
