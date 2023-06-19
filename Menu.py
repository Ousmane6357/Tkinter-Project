from tkinter import *

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='Nuevo')
filemenu.add_command(label='Abrir')
filemenu.add_command(label='Guardar')
filemenu.add_command(label='Cerrar')
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)

editmenu = Menu(menubar)
editmenu.add_command(label='Cortar')
editmenu.add_command(label='Copiar')
editmenu.add_command(label='Pegar')

helpmenu = Menu(menubar)
helpmenu.add_command(label='Contenido de ayuda')
helpmenu.add_command(label='Buscar ayuda')
helpmenu.add_separator()
helpmenu.add_command(label='Acerca de')

menubar.add_cascade(label='Archivo', menu=filemenu)
menubar.add_cascade(label='Editar', menu=editmenu)
menubar.add_cascade(label='Ayuda', menu=helpmenu)

root.mainloop()
