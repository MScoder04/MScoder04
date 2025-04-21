from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("Tkinter Image")
root.geometry("400x400")
upload=Image.open("paris.jpg")
image=ImageTk.PhotoImage(upload)
label=Label(root, image=image, height=200, width=200)
label.place(x=50,y=0)
root.mainloop()