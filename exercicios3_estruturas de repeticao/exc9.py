senha = input("Qual a senha?")
while senha!="1234":
    print ("Senha incorrecta, tente novamente!")
    senha = input("Qual a senha?")
    if senha == "1234":
        print ("Acesso Permitido!")
