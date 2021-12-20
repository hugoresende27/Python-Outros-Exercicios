# Crie uma estrutura match-case que receba uma lista com informação de um determinado pedido 
# (texto) que é associado a um código (número inteiro). Os possíveis outputs são os seguintes.
# a. Quando entra o código 200 e o pedido, aparece a mesagem: Pedido com o código 
# 200 aceite.
# b. Quando entra outro código e o pedido, aparece a mesagem: Consultar pedido com o 
# código ‘mostrar código’ no manual.
# c. Quando entra apenas o código aparece a mesagem: Falha no pedido com o código 
# ‘mostrar código’.
# d. Para outra qualquer situação aparece a mensagem: ERRO

lista = [200,'pedido']

texto = input("Qual o texto? --> ")
codigo = int(input("Qual o código? --> "))

match codigo,texto:
    case [200,"pedido"]:print("PEDIDO COM CÓDIGO 200 ACEITE")
    case [_,"pedido"]:print("CONSULTAR PEDIDO COM O CÓDIGO %d"%codigo)
    case [*_,_]:print("FALHA NO PEDIDO COM O CÓDIGO %d"%codigo)
    case _:print ("ERRO")