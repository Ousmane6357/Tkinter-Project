from tkinter import *


def selecionar():
    cadena = ''
    if (leche.get()):
        cadena += ' Con leche'
    else:
        cadena += ' Sin leche'

    if (azucar.get()):
        cadena += ' Y con azucar'
    else:
        cadena += ' Y sin azucar'

    monitor.config(text=cadena)


root = Tk()
root.title('Cafetería')
root.config(bd=15)

leche = IntVar()  # 1 si, 0 no
azucar = IntVar()  # 1 si, 0 no

imagen = PhotoImage(file='imagen.gif')  # Ruta correcta de la imagen
Label(root, image=imagen).pack(side='left')

frame = Frame(root)
frame.pack(side='left')

Label(frame, text='¿Cómo quieres el café ?').pack(anchor='w')
Checkbutton(frame, text='Con leche', variable=leche, onvalue=1, offvalue=0, command=selecionar).pack(anchor='w')
Checkbutton(frame, text='Con azucar', variable=azucar, onvalue=1, offvalue=0, command=selecionar).pack(anchor='w')

monitor = Label(frame)
monitor.pack()

# Finalmente bucle de la aplicación
root.mainloop()
