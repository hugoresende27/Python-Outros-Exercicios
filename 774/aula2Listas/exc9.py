#Programa que pesse a senha de acesso ao utilizador (1234). Enquanto a senha inserida for 
#incorretamente aparece a mensagem “Senha incorreta, tente novamente!”. Quando a senha 
#inserida for a correta aparece a mensagem “Acesso permitido!”.

senha =""
#cont = 0
while (senha != "1234"): #and (cont<=3):
    senha=input("Qual a senha? --> ")
    if (senha != "1234"):print("SENHA INCORRECTA !")
    #cont += 1
print ("ACESSO OK!")
    