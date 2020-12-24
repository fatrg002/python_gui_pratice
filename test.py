from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Nado GUI")
label1 = Label(root,text="안녕하세요")
label1.pack()

photo = PhotoImage(file="images.png")
label2 =Label(root,image=photo)
label2.pack()



root.mainloop()