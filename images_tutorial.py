from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title('Learn to code at Codemy.com')
root.iconbitmap('bird.ico')

# this will let you change icon of application, doesnt work on mac for now


my_img = ImageTk.PhotoImage(Image.open('bird.png'))

my_label = Label(image=my_img)

my_label.pack()




button_quit = Button(root, text = "Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()