from tkinter import *
def action():
    N = int(EntreyYourName1.get())
    N2 = 2*N
    EntreyYourName2.delete(0,END)
    EntreyYourName2.insert(0 , N2)


fen = Tk()
fen.geometry("400x300")
Lblnombre1 = Label(fen, text = "Enter your name1 : ")
Lblnombre1.place( x = 50, y = 50)
EntreyYourName1 = Entry(fen)
EntreyYourName1.place(x = 190, y = 50)


Lblnombre2 = Label(fen, text = "Enter your name2 : " )
Lblnombre2.place( x = 50, y = 100)
EntreyYourName2 = Entry(fen)
EntreyYourName2.place(x = 190, y = 100)

#Button:
valider = Button(fen, text = "OK" , command = action )
valider.place(x = 290, y =130)

fen.mainloop()