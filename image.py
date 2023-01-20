import tkinter
from tkinter import*
from PIL import image,ImageTk
root=Tk()
root.geometry("1000x1000")
image1=Image.open("cd.jpg")
test=ImageTk.PhotoImage(image1)
label1=tkinter.label(image=test)
label1.image=test
label1.grid(row=0,column=0)
root.mainloop()
