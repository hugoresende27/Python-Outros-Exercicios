#Programa que pesse a senha de acesso ao utilizador (1234). Enquanto a senha inserida for 
#incorretamente aparece a mensagem “Senha incorreta, tente novamente!”. Quando a senha 
#inserida for a correta aparece a mensagem “Acesso permitido!”.

senha =""
while (senha != "1234"):
    senha=input("Qual a senha? --> ")
print ("ACESSO OK!")
    