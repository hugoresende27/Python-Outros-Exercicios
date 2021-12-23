class Funcionario:
    def __init__(self,ident=0,nome="",salario=0):
        self.ident=ident
        self.nome=nome
        self.salario=salario

    def setNome(self,nome):
        self.nome=nome

    def getNome(self):
        return self.nome
#####################################################################

class Gerente(Funcionario):
    def __init__(self,ident=0,nome="",salario=0,senha=0):
        super().__init__(ident,nome,salario)
        self.senha=senha

    def setSenha(self,senha):
        self.senha=senha
        
    def getSenha(self):
        return self.senha

    def autentica (self,valor_senha):
        if valor_senha==self.senha:
            return True
        else:
            return False
#####################################################################

class Vendedor(Funcionario):
    def __init__(self,ident=0,nome="",salario=0,loja = ""):
        super().__init__(ident,nome,salario)
        self.loja=loja
        
    def setLoja(self,loja):
        self.loja=loja
        
    def getLoja(self):
        return self.loja
        
        
#####################################################################

def printDadosV(lista):
    for x in range(3):
        print (lista[x].getNome(),"\t",lista[x].getLoja()) 
        
def printDadosG(lista):
    for x in range(3):
        print (lista[x].getNome(),"\t",lista[x].getSenha()) 
        
#####################################################################

listaGer = []
listaVen = []

for x in range (3):
    listaGer.append(Gerente())
    listaVen.append(Vendedor())
    
print ("Preencha 3 Vendedores suas lojas")  

for x in range (3):
    listaVen[x].setNome(input("Qual o nome?"))
    listaVen[x].setLoja(input("Qual a loja?"))
    
  

print ("Preencha 3 Gerentes e suas passwords")   

for x in range (3):
    listaGer[x].setNome(input("Qual o seu user--> "))
    listaGer[x].setSenha(input("Defina a password--> "))
    
print ("NOME|LOJA/SENHA")
printDadosV(listaVen) 
printDadosG(listaGer) 
        
print ("Bem vindo HR Banks System")
teste = input("Qual a senha ou loja?")
for x in range(3):
    if (listaGer[x].autentica(teste)):
        print ("WELCOME MANAGER %s" %listaGer[x].getNome())
    if (listaVen[x].getLoja()==teste):
        print ("WELCOME VENDEDOR %s" %listaVen[x].getNome())
        
print ("Encerrando...")
