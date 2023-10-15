#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()

#Título de la ventana
root.title("Curso de Tkinter en Programación Fácil")

#Tamaño de la ventana, lo que va con el +, el primero es sobre las abcisas 
#y el otro las adyacentes coordenadas (X,Y)
root.geometry("500x500+500+150")

#Creación de las etiquetas
mensaje = Label(root,text="Mi primer programa con Tkinter.")
mensaje2 = Label(root,text="La segunda etiqueta que hago.")
#Se muestran las etiquetas
mensaje.pack()
mensaje2.pack()

#Bucle de ejecución
root.mainloop()