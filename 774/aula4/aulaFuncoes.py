
def minhaFuncao1():
    print ("A função começa aqui! ")
    
def func2(fnome,snome = 'teste'):
    print ("Olá Sr." + fnome.upper() + " " + snome )

def func3 (*x): #quando não sei quantos parametros vão ser passados, * transforma numa lista
    print (x[-1])
    
def func4(**y):
    print (y)
   
print ("=============================") 
print ("O programa Iniciou ")
minhaFuncao1()

print ("=============================")
n = 'hugo' #input("Nome? ")
s = 'resende' #input("Sobrenome? ")
func2(n)

print ("=============================")
func3(1,2,3,4,5,6,7,8,9)

print ("=============================")
func2(fnome ="Zecas", snome="Tobias")

print ("=============================")
# Python program to illustrate 
# *kwargs for variable number of keyword arguments
 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
print ("=============================")
myFun(first ='Geeks', mid ='for', last='Geeks') 


# Python program to illustrate 
# *args for variable number of arguments
def myFun2(*argv):
    for arg in argv:
        print (arg)
print ("=============================")
myFun2('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def func7 (pais = "PT"):
    print ("Nacionalidade:: ",pais)
print ("=============================")
func7()
print ("=============================")
func7("BRASIL")


def func5(food):
    for x in food:
        print (x)

print ("=============================")
frutas = ['uva','banana','pera']
func5(frutas)  

def func6 (x=1):
    return 5 * x 

print ("=============================")
print (func6(10))  
print (func6(1))  
print (func6(69))  
print (func6())  