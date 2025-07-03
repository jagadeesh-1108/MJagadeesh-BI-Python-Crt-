import tkinter as tk
r=tk.Tk()
r.title('Vignan')
button= tk.Button(r, text='submit',width=50,command=r.destroy)
button.pack()
button= tk.Button(r, text='enter',width=50,command=r.destroy)
button.pack()
r.mainloop()
