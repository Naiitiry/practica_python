import os
from tkinter import *
from PIL import ImageTk,Image
# Carpeta raíz
ruta = os.path.dirname(__file__)
# Carpeta de imagenes
ruta_imagen = os.path.join(ruta,"imagen14")
print(ruta_imagen)
# Iniciamos la ventana
root = Tk()
root.title("Programa de Tkinter con imagenes")

# Carga de imagenes
astronomia = ImageTk.PhotoImage(Image.open(os.path.join(ruta_imagen,"astronomia.jpg")).resize((400,200)))
avenida = ImageTk.PhotoImage(Image.open(os.path.join(ruta_imagen,"avenida.jpg")).resize((400,200)))
bosque = ImageTk.PhotoImage(Image.open(os.path.join(ruta_imagen,"bosque.jpg")).resize((400,200)))
polinesia = ImageTk.PhotoImage(Image.open(os.path.join(ruta_imagen,"polinesia.jpg")).resize((400,200)))
# Mostramos la imagenes
etiqueta1 = Label(image=astronomia)
etiqueta2 = Label(image=avenida)
etiqueta3 = Label(image=bosque)
etiqueta4 = Label(image=polinesia)
# Las acomodamos con Grid
etiqueta1.grid(row=0,column=0)
etiqueta2.grid(row=0,column=1)
etiqueta3.grid(row=1,column=0)
etiqueta4.grid(row=1,column=1)


# Loop de ventana
root.mainloop()