from tkinter import *
from tkinter import messagebox

# Configuración de la raíz
root = Tk()

def test():
    # messagebox.showinfo("Cuisine", "Vous devez partir !")
    # messagebox.showwarning("Urgence", "Vous devez partir !")
    # messagebox.showerror("Falló", "Ha accurido un error inesperado !")
#    resultado = messagebox.askquestion("Salir", "Estas seguro  de que quieres salir sin guardar ! !")
#    if resultado == "Yes":
#       root.destroy()
    #resultado = messagebox.askokcancel("Salir", "Sobreescribir el fichero actual ! !")
    # resultado = messagebox.askyesno("Salir", "Sobreescribir el fichero actual ! !")
    # if resultado:
    #     root.destroy()

    messagebox.askretrycancel("Reintentar", "No se puede canectar")


Button(root, text='Cliquéame', command=test).pack()
root.mainloop()
