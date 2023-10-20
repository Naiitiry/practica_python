#       Estilos y marcos en Tkinter
# Importaciones
from tkinter import *

# Creación de ventana
root = Tk()
# Titulo de ventana
root.title("Estilos y marcos con Tkinter")

#   Entrada de datos
entrada = Entry(root,
                background="springgreen",
                border=3,
                foreground="red",
                width=30
                ).pack()

#   Función para el botón
def enviar():
    Label(root,
            text="Se ha pulsado el botón.",
            background="skyblue",
            width=26
            ).pack()

#   Botón de enviar
boton = Button(root,
                text="Enviar",
                command=enviar,
                background="deepskyblue",
                foreground="gray98",
                border=3,
                width=25
                ).pack()

# Bucle del programa
root.mainloop()