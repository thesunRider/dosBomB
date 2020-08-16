from tkinter import *

# pip install pillow
from PIL import Image, ImageTk





root = Tk()


root.Frame1 = Frame()
root.Frame1.place(relx=0.017, rely=0.024, relheight=0.167, relwidth=0.96)

load = Image.open("../logo.png")
load = load.resize((25, 25), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=0, y=0)

root.wm_title("Tkinter window")
root.geometry("700x700")
root.mainloop()

