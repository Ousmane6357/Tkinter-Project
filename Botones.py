from tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()) )
    borrar()

def multiplicar():
    r.set(float(n1.get()) * float(n2.get()) )
    borrar()

def restar():
    r.set(float(n1.get()) - float(n2.get()) )
    borrar()


def borrar():
    n1.set('')
    n2.set('')

# def crearLabel():
#     Label(root, text='Label creada dinamicamente').pack()

root = Tk()
root.config(bd=15)

n1= StringVar()
n2= StringVar()
r= StringVar() 

Label(root, text='Número 1').pack()
Entry(root, justify='center', textvariable=n1).pack() #Primer numero


Label(root, text='Número 2').pack()
Entry(root, justify='center', textvariable=n2).pack() #Segundo numero



Label(root, text='Resultado').pack()
Entry(root, justify='center', textvariable=r, state='disabled').pack() #Resultado

button = Button(root, text='Sumar',command=sumar).pack(side='left')
button = Button(root, text='multiplicar',command=multiplicar).pack(side='left')
button = Button(root, text='Restar',command=restar).pack(side='left')


root.mainloop()
