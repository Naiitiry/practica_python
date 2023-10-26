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
fondo = ImageTk.PhotoImage(Image.open(os.path.join(ruta_fondo,"luna.jpg")).resize((500,600)))
eti=Label(root,image=fondo)
eti.place(x=0,y=0,relwidth=1,relheight=1) # Se pone imagen de fondo

# Marco
marco=LabelFrame(root,text="d",padx=20,pady=20)
# Padding del marco
marco.grid(row=1,column=0,columnspan=2,padx=70,pady=100)

# ------------------ Entrys y botones ------------------
ent1 = Entry(marco,background="SlateGray3")
ent2 = Entry(marco,background="LightYellow4", show="*")
ent1.insert(0,"Ingrese su usuario: ")
ent2.insert(0,"Ingrese su contrasña: ")
ent1.bind("<Button-1>", lambda e: ent1.delete(0, END))
ent2.bind("<Button-1>", lambda e: ent2.delete(0, END))
ent1.grid(row=0,column=0,columnspan=2)
ent2.grid(row=1,column=0,columnspan=2)

# Función de confirmación
def boton_enviar():
    usuario = ent1.get()
    contrasenia = ent2.get()
    print(f'Bienvenido usuario: {usuario}')
# Botón de confirmación de usuario.
Button(marco,text="Confirmar",command=boton_enviar).grid(row=2,column=0,columnspan=2)

# Loop de ventana
root.mainloop()