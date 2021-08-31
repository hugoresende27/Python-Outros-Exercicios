#definir constante
DESC = 0.14

valor_hora= float(input("qual o valor hora? "))
horas = float(input("quantas horas? "))

salario = valor_hora*horas
salariod = salario - (salario * DESC)
print ("o seu salário são ", salariod, "euros")