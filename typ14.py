#   Manipulación de IMG en Tkinter
#importamos tkinter
from tkinter import *
import os
#descargar módulo Pillow, ya que no viene con Python - pip install Pillow
from PIL import ImageTk,ImageColor,Image
#-----Carga de directorio-----
#       Directorio/carpeta principal
carpeta_raiz = os.path.dirname(__file__)
print(carpeta_raiz)
#       Carpeta imagenes
#se utiliza join para unir la dirección de carpeta raiz y la carpeta de imagenes.
#si tuviera otras carpetas dentro, se agrega "imagen/paisajes", por ejemplo.
carpeta_imagenes = os.path.join(carpeta_raiz,"imagen")
#variable de la carpeta "PAISAJES" dentro de "imagen"
carpeta_paisajes = os.path.join(carpeta_imagenes,"PAISAJES")
print(carpeta_paisajes)
# print(carpeta_imagenes)
#inicializamos la ventana
root = Tk()
#Agregamos título a la ventana
root.title("Aprendiendo a manejar Tkinter")
#Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes,"favicon.ico"))

#Carga de imagen
#el método "resize" es de "Image", por lo tanto va después del segundo paréntesis y usa una tupla como coordenadas (X,Y)
bosque = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes,"bosque.jpg")).resize((350,200)))
#Mostramos la imagen
etiqueta = Label(image=bosque)
#La acomodamos
etiqueta.pack()




#lupeamos la instancia root para que se mantenga abierta la ventana.
root.mainloop()