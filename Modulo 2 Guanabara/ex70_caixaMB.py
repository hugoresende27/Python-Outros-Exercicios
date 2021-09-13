print ("\033[32;7m "+"{:=^40}".format("BANCO HR")+"\033[m")

# Python3 program to accept an amount
# and count number of notes
 
# Function to count and print
# currency notes
def countCurrency(amount):
     
    notes = [2000, 500, 200, 100,
               50, 20, 10, 5, 1]
                
    noteCounter = [0, 0, 0, 0, 0,
                     0, 0, 0, 0]
     
    print ("Currency Count -> ")
     
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print (i ," : ", j)
 
# Driver code
amount = int(input("Qual o valor? --> "))
countCurrency(amount)




print ("\033[32;7mFIM...\033[m")