#Programa que pede o nome, se é licenciado e idade ao utilizador. Se o género for licenciado 
#(resposta s ou S) e a idade superior a 30 mostra o nome da pessoa e a palavra ACEITE. Caso 
#contrário mostra NÃO ACEITE

nome = input("Qual o seu nome?--> ")
lic = str(input("É licenciado? [S/N]--> "))
ida = int(input("Idade? --> "))
if ((lic in 'sS') and (ida>30)): print ("%s com %d anos foi ACEITE"%(nome,ida))
else: print("NÂO ACEITE")