print ("\033[33;7m "+"{:=^40}".format("Programa MEDIA")+"\033[m")

sair="n"
total=0
contador=0
maior=0
menor=0
while(sair!="s"):
    num=int(input("Valor --> "))
    total+=num
    contador+=1
    if (contador==1):       #na primeira iteração (contador==1) o maior e o menor vão receber num
        maior=menor=num
    else:
        if (num>maior):         #se num maior do que maior, var maior passa a ser o num
            maior=num
        if (num<menor):         #se num menor do que o menor, var menor passa a ser o num
            menor=num
    sair=str(input("\033[34;7mQuer sair? (s/n)--> \033[m")).lower().strip() [0] #[0] considerar só a primeira letra

print ("Total números {}".format(contador))
print ("Soma total {}".format(total))
media=total/contador
print ("Média {}".format(media))

print ("O maior valor foi o {} e menor foi {}".format(maior,menor))

