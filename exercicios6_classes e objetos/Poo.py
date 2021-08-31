class Pessoa:
    def __init__(objeto,nome="",idade=0): #assinatura construtor (objeto pode ser self etc, nome idade) 
        objeto.nome=nome                  #atributo/caracteristicas da classe   ="" e =0, valor por defeito construir vazio
        objeto.idade=idade                #atributo da classe

                                        #abstrato
    def func(objeto):
        print ("Olá o meu nome é " +objeto.nome)
#cria o objeto pessoa 1
p1= Pessoa("Maria",20)                  #concreto

print (p1)
print (p1.nome)
print (p1.idade)
p1.func()
p1.idade=22
print (p1.idade)

p2=Pessoa("João", 40)
print (p2.nome)

p3=Pessoa()
p3.nome="Pedro"
print (p3.nome)