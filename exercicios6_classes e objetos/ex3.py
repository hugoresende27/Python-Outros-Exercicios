class Funcionario:
    def __init__(self,ident=0,nome="",salario=0):
        self.ident=ident
        self.nome=nome
        self.salario=salario

    def setNome(self,nome):
        self.nome=nome

    def mostraNome(self):
        return self.nome

class Gerente(Funcionario):
    def __init__(self,ident=0,nome="",salario=0,senha=0):
        super().__init__(ident,nome,salario)
        self.senha=senha

    def setSenha(self,senha):
        self.senha=senha

    def autentica (self,valor_senha):
        if valor_senha==self.senha:
            print ("Acesso Permitido")
            return True
        else:
            print ("Acesso negado")
            return False
        
ger1=Gerente()
print (ger1.nome)

ger1.setNome("Hugo")
ger1.setSenha("1234")

print ("TESTE SENHA :: " ,(ger1.autentica("1234")))
print (ger1.mostraNome())