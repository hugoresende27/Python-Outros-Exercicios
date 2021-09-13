print ("\033[36;7m "+"{:=^40}".format("BANCO HR V2")+"\033[m")

valor = int(input("Quanto quer sacar?? € "))
total = valor
nota=50                                                 #consideramos começar com a var nota a valer 50
total_notas=0                                           #total das notas é 0
while True:
    if total>=nota:                                     #se total, na 1ªiteração valor total for maior que nota, ex: 950 >= 50
        total-=nota                                     #980=980-50 = 930           930=930-50 = 880
        total_notas+=1                                  #total de notas(50) = 1     total de notas(50) = 2
    else:                   #quando o total for menor do que 50, valor da var nota até aqui
        if total_notas>0:#só vai dar print se houver mais do que 0 notas no total_notas
            print (f"Total de {total_notas} notas de {nota} €€")    #print de ex: 19 notas de 50
        if nota==50:                    #se a nota for 50, passa a valer 20 e volta ao inicio do ciclo
            nota=20                                     #no inicio do ciclo novamente, agora var nota vale 20, ex: 30 >= 20
        elif nota == 20:                                                            #30=30-20 = 10              
            nota =10                                                                #total de notas(20) = 1     
        elif nota == 10:                                #quando total, agr 10, for menor ou igual que nota, era 20 agr é 10
            nota = 1                                                                #10=10-10 = 0
        total_notas=0                                                               #total de notas(10) = 1
        if total==0:                                    #quando o total for 0 break
            break

    
print ("\033[31;7mFIM...\033[m")
