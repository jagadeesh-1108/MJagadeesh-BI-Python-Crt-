from tkinter import *
master=Tk()
w=Scale(master,from_=0,to=42)
w.pack()
w=Scale(master,from_=0,to=200, orient=HORIZONTAL)
w.pack()
mainloop()
#for zoom in and zoom out and size adjustment