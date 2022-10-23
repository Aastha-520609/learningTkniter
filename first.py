from tkinter import *
root = Tk()
#pack method, disadvan - it doesn't give total hands on work here
#myLabel =Label(root, text="Hello World")
#myLabel.pack()
#grid method
myLabel1 = Label(root, text = "Hello World")
myLabel2 = Label(root, text = "My name is Aastha Chaudhary")
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)
root.mainloop()
