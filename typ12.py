#   *****   Eventos de mouse y teclado de tkinter *****

#Importaciones
from tkinter import *

#Creación de la pantalla principal
root = Tk()

#Título de la pantalla
root.title("Curso de Tkinter de Programación")

#Widget
entrada = Entry(root)

#se usa insert para que aparesca un texto como figura abajo en el cuadro que escribimos
entrada.insert(0,"Escribir su nombre...")

#sirve para, cuando hacemos clic para escribir, borrar lo que pusimos con insert (método de arriba).
entrada.bind("<Button-1>", lambda e: entrada.delete(0, END))
#aplicar un lambda para que cuando se haga clic recién lo borre y no a penas se ejecuta la app.
#entrada.bind("<Key>", lambda e: entrada.delete(0, END)) --> cuando hago clic y despues presiono cualquier
#tecla se borra todo en donde ingresaría el texto. Pero me borra todo mientras voy escribiendo.

entrada.pack()

#Evento del botón
def pulsar_boton():
    #el método get() pertenece a Entry()
    nombre = entrada.get()
    Label(root,text=f'{nombre}').pack()

#Botón
Button(root,text="Enviar!",command=pulsar_boton).pack()

#Bucle de ejecución
root.mainloop()