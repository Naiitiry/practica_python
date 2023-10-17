"""  ********************    Ejercicios 1 y 2    ********************  """
"""
#importaciones
from tkinter import*

#muestra de ventana en pantalla
root = Tk()
root.title = "Práctica de Tkinter"

#función
def accion_boton(numero_boton):
    etiqueta = Label(root,text=f'Se ha presionado el botón {numero_boton}.')
    etiqueta.pack()

#botones
Button(root, text="Boton 1",command=lambda:accion_boton(1)).pack()
Button(root, text="Boton 1",command=lambda:accion_boton(2)).pack()
Button(root, text="Boton 1",command=lambda:accion_boton(3)).pack()
Button(root, text="Boton 1",command=lambda:accion_boton(4)).pack()

root.mainloop()
#loop para que no se cierre
"""

#       ***************     Ejercicio 3     ***************
#importaciones
from tkinter import *

#inicio de programa
root = Tk()
root.title("Programa de nombre y apellido")

#entry para nombre y edad
entrada1 = Entry(root)
entrada2 = Entry(root)
#formateamos los Entrys para indicar que pide c/u
entrada1.insert(0,"Ingrese su nombre:")
entrada2.insert(0,"Ingrese su edad:")
#funcion para limpiar Entry al hacer clic izquierdo
entrada1.bind("<Button-1>",lambda e:entrada1.delete(0,END))
entrada2.bind("<Button-1>",lambda e:entrada2.delete(0,END))
#posicionamos los Entrys
entrada1.grid(row=0,column=1)
entrada2.grid(row=1,column=1)
#creamos los Labels para cada Entry.
nombre = Label(root,text="Nombre:").grid(row=0,column=0)
edad = Label(root,text="Edad:").grid(row=1,column=0)

#Evento del botón.
def evento_boton():
    nombre = entrada1.get()
    edad = entrada2.get()
    Label(root,text=f'Mi nombre es {nombre} y tengo {edad} años.').grid(row=3)

#botón
Button(root,text="Botón",command= lambda: evento_boton()).grid(row=2,column=1)

#bucle de programa
root.mainloop()