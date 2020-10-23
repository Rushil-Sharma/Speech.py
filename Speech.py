import pyttsx3
from tkinter import *
Google_Assistent = pyttsx3.init()
root = Tk()
speak = Entry(root,font=('Helvatica',30),fg='light blue',bg='dark blue')
speak.grid(row=1,column=1)
def x():
    a = (speak.get())
    Google_Assistent.say(a)
    Google_Assistent.runAndWait()
Run = Button(root,text='Next',font=('Helvatica',30),fg='light blue',bg='dark blue',command=x)
Run.grid(row=2,column=1)
root.mainloop()