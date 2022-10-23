from tkinter import*
#import tkinter
#from tkinter import ttk
root = Tk()
#creating
#1. if we want to make the button unclickable then we will put state as disabled, initially it is enabled.
#2. if we want to change the size of button then we can do it manually by pad x and pad y method. (it is like padding in html)
#3. To show the content after clicking the button, we use command widgets. For that we have to make an funtion which actually does 
# the work and the call the function in command widget.
#4. For changing the colour of text fg is used and for changing the background bg is used.
def myClick() :
    myLabel = Label(root, text = "I just clicked the button", fg = "blue")
    myLabel.pack()

myButton = Button(root, text = "Click Me!", command = myClick, fg="red", bg="yellow")  
#putting up on the screen
myButton.pack()
root.mainloop()             

