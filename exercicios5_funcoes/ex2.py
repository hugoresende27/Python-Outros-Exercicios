def qual_maior(num1,num2):
    if num1>num2:
        print (" %s é maior"%num1)
    elif num1<num2:
        print (" %s é maior"%num2)
    else:
        print ("São Iguais")




############# com return

def maior (num1,num2):
    if num1>num2:
        return num1
    elif num1<num2:
        return num2
    else:
        return (num1,num2)  




############# com max
def maior2 (num1,num2):
    return max(num1,num2)


num1=float(input("NR 1 :: "))
num2=float(input("NR 2 :: "))
qual_maior(num1,num2)
print (maior(num1,num2))
print (maior2(num1,num2))

qual_maior(int(input("Num 1:: ")),int(input("Num 2:: ")))