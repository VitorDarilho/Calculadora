from tkinter import *

root = Tk()

root.title('Sua calculadora')
root.geometry('400x355')
root.minimize(400,355)
root.maximize(400,355)

root.configure(background='#282828')

e= Entry(root, width= 15, borderwidth= 4, relief=FLAT)
root.miniloop()
