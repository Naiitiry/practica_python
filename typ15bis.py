from tkinter import *

root = Tk()
root.title("Estilos y marcos en Tkinter")

#   Marco agregamos margenes internos del MARCO
marco = LabelFrame(root,text="Marco de ventana principal",padx=20,pady=20)
# agregamos padding al marco
marco.pack(padx=15,pady=15)
#   Entrada de datos en MARCO
entrada = Entry(marco,
                background="springgreen",
                border=3,
                foreground="red",
                width=30
                ).pack()

#   Función para el botón en el MARCO
def enviar():
    Label(marco,
            text="Se ha pulsado el botón.",
            background="skyblue",
            width=26
            ).pack()

#   Botón de enviar en MARCO
boton = Button(marco,
                text="Enviar",
                command=enviar,
                background="deepskyblue",
                foreground="gray98",
                border=3,
                width=25
                ).pack()

root.mainloop()