from tkinter import *

count = 0
def click():
    global count
    count+=1
    print(count)

root = Tk()

button = Button(root, text="Click me", font=("arial", 20) , command = click, fg = "#00ff00", bg="black", activeforeground="#00ff00", activebackground="blue")

button.pack()

root.mainloop()