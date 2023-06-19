from tkinter import *

root = Tk()
root.title('Hola mundo')
root.iconbitmap('./hola.ico')
# root.resizable(False,False)

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")



root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")


#Finaliza el bucle de la aplicacion
root.mainloop()
