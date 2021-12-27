from tkinter import *
window = Tk()
def from_kg():
    #kg para gr
    gram = float (e2_value.get())*1000
    #kg para pound
    pound = float (e2_value.get())*2.20462
    #kg para onça
    onca = float (e2_value.get())*35.274
    
    #########INSERE O TEXTO CONVERTIDO NA TEXT WIDGET##########
    t1.delete("1.0",END)
    t1.insert(END,gram)
    
    t2.delete("1.0",END)
    t2.insert(END,pound)
    
    t3.delete("1.0",END)
    t3.insert(END,onca)
    
#############LABEL WIDGETS#############
e1 = Label(window, text="Insira o peso em Kg's")
e2_value=StringVar()
e2 =Entry (window, textvariable=e2_value)
e3=Label(window,text="Gramas")
e4=Label(window,text="Pounds")
e5=Label(window,text="Onças")

##############TEXT WIDGETS###################

t1 = Text(window, height=1,width=20)
t2 = Text(window, height=1,width=20)
t3 = Text(window, height=1,width=20)

############BOTÃO WIDGET#################
b1 = Button(window,text="Converter", command=from_kg)

##################GRELHA ##############

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

###########star windows##############
window.mainloop()