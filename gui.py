from tkinter import *

root = Tk()

#creat a label widget

#myLabel = Label(root, text = "Hello World")
#myLabel2 = Label(root, text = "My name is Raul Bazan")

#shove label into screen

#myLabel.grid(row = 0, column = 0)
#myLabel2.grid(row = 1, column = 1 )


# to create an entry
e = Entry(root, width = 50)

e.pack()
e.insert(0, "Enter your name")
# get function retrieves data


def myClick():
	hello = "hello " + e.get()
	# you can insert variable
	myLabel1 = Label(root, text = hello)
	myLabel1.pack()

# padx, pady will change size of button, state = Disabled will grey out button
myButton = Button(root, text = "Enter your name", command = myClick)

myButton.pack()

root.mainloop()



