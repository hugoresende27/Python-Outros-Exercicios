class Funcionario:
    def __init__(self,ident=0,nome="",salario=0):
        self.ident=ident
        self.nome=nome
        self.salario=salario

    def setNome(self,nome):
        self.nome=nome

    def getNome(self):
        return self.nome

class Gerente(Funcionario):
    def __init__(self,ident=0,nome="",salario=0,senha=0):
        super().__init__(ident,nome,salario)
        self.senha=senha

    def setSenha(self,senha):
        self.senha=senha

    def autentica (self,valor_senha):
        if valor_senha==self.senha:
            return True
        else:
            return False

lista = []

for x in range (3):
    lista.append(Gerente())
    
print ("Preencha 3 users e 3 passwords")   

for x in range (3):
    lista[x].setNome(input("Qual o seu user--> "))
    lista[x].setSenha(input("Defina a password--> "))
        
print ("Bem vindo HR Banks System")
teste = input("Qual a senha? ")
for x in range(3):
    if (lista[x].autentica(teste)):
        print ("WELCOME MANAGER %s" %lista[x].getNome())
        
print ("Encerrando...")
