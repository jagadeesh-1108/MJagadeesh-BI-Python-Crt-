from tkinter import *
root = Tk()
scrollbar= Scrollbar (root)
scrollbar.pack(side =RIGHT, fill = Y)
mylist =Listbox(root, yscrollcommand= scrollbar.set)
for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
mylist.pack(side=LEFT, fill= BOTH)
scrollbar.config(command = mylist.yview)
mainloop()
#scroll is used for scrolling or  moving down and upwards  without adjusting size 