from tkinter import *
master = Tk()
w = Canvas(master, width=43,height=60)
w.pack()
Canvas_height=20
Canvas_Width=200
y=int(Canvas_height/2)
w.create_line(0,y,Canvas_Width,y)
mainloop()
