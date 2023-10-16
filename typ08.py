# Importaciones
from tkinter import *

#Creación ed la ventana principal
root = Tk()

#Creación de la etiqueta
mensaje = Label(root, text="Mi primer programa con Tkinter.")

#Muestra de etiqueta
mensaje.pack()

#Bucle de ejecución
root.mainloop()