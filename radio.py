from tkinter import *
from PIL import ImageTk, ImageTk
root = Tk()
root.title("Radio")


#r = IntVar()
#r.set("2")

def click(value):
	myLabel = Label(root, text = pizza.get())
	myLabel.pack()


TOPPINGS =[
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
]

pizza = StringVar()

#pizza.set("Pepperoni")

for text, toppings in TOPPINGS:
	Radiobutton(root, text = text, variable = pizza, value = toppings).pack(anchor = W)
#Radiobutton(root, text = "Option 1", variable = r, value =1, command=lambda: click(r.get())).pack()
#Radiobutton(root, text = "Option 2", variable = r, value =2, command=lambda: click(r.get())).pack()



#myLabel = Label(root, text = pizza.get())
#myLabel.pack()

mybutton = Button(root, text = "click me", command = lambda: click(pizza.get()))
mybutton.pack()

mainloop()

