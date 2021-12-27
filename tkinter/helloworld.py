from tkinter import *
window = Tk()

e1 = Label(window, text="Nome")
e2_value=StringVar()
e2 =Entry (window, textvariable=e2_value)
t1 = Text(window, height=1,width=20)

# t1.delete("1.0",END)
#t1.insert(END,t1)

b1 = Button(window,text="Hello", command=t1.insert(END,e2_value))


e1.grid(row=0, column=0)
t1.grid(row=2, column=0)
e2.grid(row=0, column=1)
b1.grid(row=0, column=2)


window.mainloop()