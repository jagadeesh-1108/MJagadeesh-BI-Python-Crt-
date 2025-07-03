from tkinter import *
top = Tk()
# Create Menubutton
mb = Menubutton(top, text="Course", relief=RAISED)
mb.grid()
# Create a menu for the Menubutton
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
# Create IntVar variables
mayoVar = IntVar()
ketchVar = IntVar()
# Add checkbuttons to the menu
mb.menu.add_checkbutton(label="Btech", variable=mayoVar)
mb.menu.add_checkbutton(label="Bsc", variable=ketchVar)
top.mainloop()