from tkinter import *
from PIL import Image,ImageTk
import os
#-----Carga de directorio-----
# Importamos carpeta origen
carpeta_raiz = os.path.dirname(__file__)
# Buscamos la carpeta de imagenes
carpeta_imagenes = os.path.join(carpeta_raiz,"imagen16")
# Carpeta de botón
boton_imagen = os.path.join(carpeta_imagenes,"boton")
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
bandera1 = Label(marco,image=argentina,background="NavajoWhite2")
bandera1.grid(row=0,column=0)
# -------------- Australia --------------
australia = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes,"australia.png")).resize((200,100)))
bandera2 = Label(marco,image=australia,background="NavajoWhite2")
bandera2.grid(row=0,column=1)
# -------------- España --------------
españa = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes,"espana.png")).resize((200,100)))
bandera3 = Label(marco,image=españa,background="NavajoWhite2")
bandera3.grid(row=2,column=0)
# -------------- Estonia --------------
estonia = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes,"estonia.png")).resize((200,100)))
bandera4 = Label(marco,image=estonia,background="NavajoWhite2")
bandera4.grid(row=2,column=1)
# Variable de Control
opcion = StringVar()
opcion.set("Error")

# Radiobuttons

Radiobutton(marco,text="Argentina",variable=opcion,background="dark turquoise",value="Argentina").grid(row=1,column=0)
Radiobutton(marco,text="Australia",variable=opcion,background="dark slate blue",value="Australia").grid(row=1,column=1)
Radiobutton(marco,text="España",variable=opcion,background="coral2",value="España").grid(row=3,column=0)
Radiobutton(marco,text="Estonia",variable=opcion,background="RoyalBlue1",value="Estonia").grid(row=3,column=1)

# ---------------- Ejercicio opcional ----------------
# Imagen del boton
boton_entrar = ImageTk.PhotoImage(Image.open(os.path.join
                (boton_imagen,"button.png")))
# ------------- Función del botón -------------
def boton_selecccion():
    if opcion.get()=="Error":
        Label(root,
        text=f'No has seleccionado ninguna cuenta, por favor, elige una',
        background="gray98",
        foreground="red2").pack()
    else:
        Label(root,
        text=f'Hola {opcion.get()}. Accediendo a tu cuenta personal...',
        background="gray98").pack()
        print(opcion.get())
# Botón
boton = Button(root,
        text="Entrar",
        image=boton_entrar,
        border=0,
        command=boton_selecccion,
        background="NavajoWhite2").pack(pady=10)



root.mainloop()