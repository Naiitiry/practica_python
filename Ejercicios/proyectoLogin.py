#               PRACTICA DÍA 14

import os
from tkinter import *
from PIL import ImageTk,Image
from getpass import *

# Carpeta raíz
ruta = os.path.dirname(__file__)
# Carpeta iconos e imagen
ruta_imagen = os.path.join(ruta,"imagen14")
# Inicio de programa
root = Tk()
root.title("Proyecto n° 1 - Login")
# Icono de ventana
root.iconbitmap(os.path.join(ruta_imagen,"favicon.ico"))

#           Contenido de ventana del programa
# Logo de programa
logo = ImageTk.PhotoImage(Image.open(os.path.join(ruta_imagen,"american-rider.png")).resize((300,225)))
etiqueta1 = Label(image=logo)
etiqueta1.pack()

#           Casillas de usuario y contraseña
# Usuario
Label(text="Usuario").pack()
entrada1 = Entry()
entrada1.insert(0,"Ej.: Laura")
entrada1.bind("<Button-1>", lambda e: entrada1.delete(0, END))
entrada1.pack()

# Contraseña
Label(text="Contraseña").pack()
entrada2 = Entry()
entrada2.insert(0,"*"*7)
entrada2.bind("<Button-1>", lambda e: entrada2.delete(0, END))
entrada2.pack()

# Usuario creado
usuario_creado = ()

# Metemos todo dentro de un While
while True:
    # Pide usuario y contraseña en LA CONSOLA
    nuevo_usuario = input("Ingrese usuario: ")
    nueva_contraseña = getpass("Ingrese contraseña: ")
    # Se pide nuevamente los datos
    repite_usuario = input("Ingrese, nuevamente, su usuario: ")
    repite_contraseña = getpass("Ingrese, nuevamente, su contraseña: ")

    # Condicionales para verificar correcto ingreso de datos
    if nuevo_usuario!=repite_usuario or nueva_contraseña!=repite_contraseña:
        print("Los datos proporcionados no coinciden.")
    else:
        usuario_creado = (nuevo_usuario,nueva_contraseña)
        break

# Evento del botón
def validar():
    usuario = entrada1.get()
    contraseña = entrada2.get()
    if usuario!=usuario_creado[0] or contraseña!=usuario_creado[1]:
        Label(text="Usuario o contraseña erroneos.").pack()
    else:
        Label(text=f'Hola {usuario_creado[0]}. Espere mientras carga el programa.').pack()
# Botón
Button(text="Validar",command=validar).pack()

root.mainloop()