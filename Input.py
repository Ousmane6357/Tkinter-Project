from tkinter import *

root = Tk()

label = Label(root, text='Nombre')
label.grid(row=0, column=0, sticky='e',padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1,padx=5, pady=5)
entry.config(justify='center')

label2 = Label(root, text='Apellido')  # Corrección en esta línea
label2.grid(row=1, column=0, sticky='e',padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1,padx=5, pady=5)


label3 = Label(root, text='Contraseña')  # Corrección en esta línea
label3.grid(row=2, column=0, sticky='e',padx=5, pady=5)

entry3 = Entry(root)
entry3.grid(row=2, column=1,padx=5, pady=5)
entry3.config(justify='center', show='?')


root.mainloop()
