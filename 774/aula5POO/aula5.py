
from pessoa import Pessoa
from professor import Professor
from aluno import Aluno

prof1 = Professor("Pedro",55,"Matemática")
prof1.print1()
prof1.setdisciplina("Programação")
prof1.print1()


aluno1 = Aluno("Tozé",15,"Turma C")
aluno1.print1()
aluno1.setturma("Turma A")
aluno1.print1()


'''
p1 = Pessoa ("Hugo",33)
print (p1.nome)
p1.setNome("Tó")
print (p1.nome)
print("========================")

p2  = Pessoa ()

p2.setIdade(int(input("Qual a idade?-->")))
p2.setNome(input("Qual o nome? -> "))
p2.print1()
'''

'''
lista = []

for x in range (3):
    lista.append(Pessoa())

for x in range(3):
    lista[x].setIdade(int(input("Qual a idade?-->")))
    lista[x].setNome(input("Qual o nome? -> "))

for x in range(3):
    lista[x].print1()
'''

