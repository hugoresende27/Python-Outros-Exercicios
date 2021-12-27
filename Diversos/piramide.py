print ("TRIÂNGULO COM ESTRELAS")
size = int(input("Qual o tamanho? --> "))
m = (2* size)-2
for i in range (0,size):
    for j in range(0,m):
        print(end="")
    m = m- 1 #decremento
    for j in range(0,i+1):
        print("*", end='')
    print ("")