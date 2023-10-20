from tkinter import *

root=Tk()
root.title("Ejercicios de Variables de control y Radiobuttons")

# Variable de Control
opcion = IntVar()

# Radiobuttons
Radiobutton(root,text="Ricardo",variable=opcion,value=1).grid(row=0,column=0)
Radiobutton(root,text="Hernesto",variable=opcion,value=2).grid(row=0,column=1)
Radiobutton(root,text="Paula",variable=opcion,value=3).grid(row=1,column=0)
Radiobutton(root,text="Micaela",variable=opcion,value=4).grid(row=1,column=1)



root.mainloop()