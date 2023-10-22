from tkinter import *
from PIL import Image,ImageTk
import os
#-----Carga de directorio-----
# Importamos carpeta origen
carpeta_raiz = os.path.dirname(__file__)
# Buscamos la carpeta de imagenes
carpeta_imagenes = os.path.join(carpeta_raiz,"imagen16")
# ------- Inicio de Program -------
root=Tk()
root.title("Ejercicios de Variables de control y Radiobuttons")
root.configure(background="SlateGray2")
# ------------- MARCO -------------
marco = LabelFrame(root,text="Marco de las imagenes",padx=10,pady=10,background="NavajoWhite2",border=0)
marco.pack(padx=15,pady=15)

# Asignamos las imagenes en variables
# -------------- Argentina --------------
argentina = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes,"argentina.png")).resize((200,100)))
bandera1 = Label(marco,image=argentina)
bandera1.grid(row=0,column=0)
# -------------- Australia --------------
australia = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes,"australia.png")).resize((200,100)))
bandera2 = Label(marco,image=australia)
bandera2.grid(row=0,column=1)
# -------------- España --------------
españa = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes,"espana.png")).resize((200,100)))
bandera3 = Label(marco,image=españa)
bandera3.grid(row=2,column=0)
# -------------- Estonia --------------
estonia = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes,"estonia.png")).resize((200,100)))
bandera4 = Label(marco,image=estonia)
bandera4.grid(row=2,column=1)
# Variable de Control
opcion = IntVar()

# Radiobuttons

Radiobutton(marco,text="Argentina",variable=opcion,background="dark turquoise",value=1).grid(row=1,column=0)
Radiobutton(marco,text="Australia",variable=opcion,background="dark slate blue",value=2).grid(row=1,column=1)
Radiobutton(marco,text="España",variable=opcion,background="coral2",value=3).grid(row=3,column=0)
Radiobutton(marco,text="Estonia",variable=opcion,background="RoyalBlue1",value=4).grid(row=3,column=1)



root.mainloop()