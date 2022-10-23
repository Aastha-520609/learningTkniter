from tkinter import*
root = Tk()

#1. Entry widget is used for input
#2. Working with input data. Insert method shows text inside the box
e = Entry(root, width = 30, borderwidth = 5)
#e.pack()
e.grid(row=0, column =1)
e.insert(1,"Enter Your Name")
myLabel = Label(root, text= "Username")
#myLabel.pack()
myLabel.grid(row=0, column = 0)
#myButton = Button(root, text = "Click Me!")
#myButton.pack()

root.mainloop()

