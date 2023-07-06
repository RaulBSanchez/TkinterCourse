from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('YouTube Tutorial')

frame = LabelFrame(root, padx = 50, pady = 50)

frame.pack(padx=10, pady=10)

# put butotn in frame
button = Button(frame, text = "dont click here")

button.pack()



root.mainloop()