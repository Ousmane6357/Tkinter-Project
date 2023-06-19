from tkinter import *

# Configuración de la raíz
root = Tk()
"""""
#Variables 
texto = StringVar()
texto.set('La belle vie')

# Configuración de un marco
frame = Frame(root, width=480, height=320)
frame.pack()

Label(frame, text='Hola mundo').pack(anchor='nw')
label = Label(frame, text='Otra etiqueta')
label.pack(anchor='center')
Label(frame, text='Ultima etiqueta').pack(anchor='se')

label.config(bg='green', fg="white", font=('verdana',24))
label.config(textvariable=texto)
"""

image = PhotoImage(file='./imagen.gif')
Label(root, image=image, bd=0).pack(side='left')
# Finaliza el bucle de la aplicación
root.mainloop()
