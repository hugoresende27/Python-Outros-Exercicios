#conceito simples de herança
#classe Pai
class Pessoa:
    def __init__(objeto,nome="",idade=0):
        objeto.nome=nome
        objeto.idade=idade

    def mostraNome(objeto):
        print ("Olá o meu nome é "+objeto.nome)

#classe Filho
class Estudante(Pessoa):
    pass                        #palavra chave para passar

estudante1=Estudante("Rui",30)
print (estudante1.nome)

estudante2=Estudante()
print (estudante2.nome)

pessoa1=Pessoa()
print (pessoa1.idade)