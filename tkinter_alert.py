from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400")
messagebox.showwarning("Window Name","Alert!")
def msg():
    messagebox.showwarning("alert","Stop! Virus found!")
button=Button(root,text="Scan for virus",command=msg)
button.place(x=40,y=80)
root.mainloop()