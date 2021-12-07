#. Programa que pede a idade de uma pessoa e informa a sua classe eleitoral. (Não-eleitor (abaixo 
#de 16 anos); Eleitor obrigatório (dos 18 aos 65 anos, inclusivé); Eleitor facultativo (dos 16 aos 18 
#e maiores de 65 anos).


idade = int(input("idade--> "))
if (idade<16): print("NAO ELEITOR")
elif (18<=idade<=65): print("OBRIGATÓRIO")
elif (16<idade<18) or idade>65: print("FACULTATIVO")