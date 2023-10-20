import os
from tkinter import *
from PIL import ImageTk,Image

# Ruta principal
ruta = os.path.dirname(__file__)
# Ruta de imagenes
ruta_imagen = os.path.join(ruta,"imagenproyecto1")
ruta_fondo = os.path.join(ruta_imagen,"fondo")

# Iniciamos el programa
root = Tk()
# Titulo de programa
root.title("Mini proyecto 1")

# Icono de ventana
root.iconbitmap(os.path.join(ruta_imagen,"avocado.ico"))
# Carga de imagenes
fondo = ImageTk.PhotoImage(Image.open(os.path.join(ruta_fondo,"luna.jpg")).resize((300,400)))
eti=Label(image=fondo)
eti.pack()
# Entris y botones
ent1 = Entry(root)
ent2 = Entry(root)
ent1.insert(0,"x")
ent2.insert(0,"y")
ent1.bind()
ent2.bind()

# Loop de ventana
root.mainloop()