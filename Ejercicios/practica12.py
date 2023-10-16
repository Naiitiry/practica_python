#importaciones
from tkinter import *
#ventana principal
root = Tk()
#Titulo de programa
root.title = "Práctica con Tkinter"
#función de botón
def crear_etiqueta(numero_boton):
    etiqueta = Label(root,text=f'Botón {numero_boton} pulsado.')
    etiqueta.pack()

#Botones
Button(root,text="Botón 1",command=lambda:crear_etiqueta(1)).pack()
Button(root,text="Botón 2",command=lambda:crear_etiqueta(2)).pack()
Button(root,text="Botón 3",command=lambda:crear_etiqueta(3)).pack()
Button(root,text="Botón 4",command=lambda:crear_etiqueta(4)).pack()
"""
Button(root,text="Botón 1",command=lambda:crear_etiqueta(1)).grid(row=0,column=0)
Button(root,text="Botón 2",command=lambda:crear_etiqueta(2)).grid(row=1,column=0)
Button(root,text="Botón 3",command=lambda:crear_etiqueta(3)).grid(row=2,column=0)
Button(root,text="Botón 4",command=lambda:crear_etiqueta(4)).grid(row=3,column=0)
"""

#bucle de ejecución
root.mainloop()