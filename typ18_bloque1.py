# -------------------------------- MESSAGEBOX ------------------------------------------------

# Ventanas de alerta, en su mayoría, damos avisos al usuario

from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Teoría 18, Bloque 1")

def muestra_info():
    # Mostramos las diferentes ventanas de alerta que tiene el módulo
    showinfo("Hola locura, como estas?","Recatate amiiiiiii")
    #showwarning("Cuidaditoooo!","Recatate amiiiiiii")
    #showerror("No está bien eso!","Recatate amiiiiiii")
    #askquestion("No está bien eso!","Recatate amiiiiiii")
    #askyesno("No está bien eso!","Recatate amiiiiiii")
    #askokcancel("No está bien eso!","Recatate amiiiiiii")
    #askyesnocancel("No está bien eso!","Recatate amiiiiiii")
    #askretrycancel("Algo salió para el tujes","No se pudo hacer eso")


boton = Button(root,text="Enviar",width=75,command=muestra_info).pack()

root.mainloop()