from tkinter import *

main = Tk()

ourMessage = 'This is Vrbest Python gui Class'

messageVar= Message(main, text = ourMessage, width=1000)

messageVar.config(bg='red')

messageVar.pack()

main.mainloop()