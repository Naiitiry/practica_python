#               Radiobuttons y Variables de Control.
#importaciones
from tkinter import *

root = Tk()
root.title("Programación con Python y Tkinter n° 16")

# Variable de control
opcion = IntVar()
# Seteamos la variable de control
opcion.set(2)
# Función para devolver que valor se elige
def actualiza_radio(valor):
    Label(root,text=valor).pack()

# Radiobutton
Radiobutton(root,text="Rojo",variable=opcion,value=1).pack()
Radiobutton(root,text="Verde",variable=opcion,value=2).pack()
Radiobutton(root,text="Naranja",variable=opcion,value=3).pack()
Radiobutton(root,text="Violeta",variable=opcion,value=4).pack()
Radiobutton(root,text="Azul",variable=opcion,value=5).pack()
Radiobutton(root,text="Amarillo",variable=opcion,value=6).pack()

# Botón de envio
boton_envio = Button(root,text="Enviar",command=lambda:actualiza_radio(opcion.get())).pack()

Label(root,text=f'{opcion.get()}').pack()
# Bucle del programa
root.mainloop()