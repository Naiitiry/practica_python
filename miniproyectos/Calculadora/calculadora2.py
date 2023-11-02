from tkinter import*


root = Tk()
root.title("Calculadora básica")
root.geometry('500x666+400+20')
# para que la ventana no se pueda redimensionar
root.resizable(width=FALSE,height=FALSE)
root.configure(background="purple3")

# Entry donde recibe los valores.
# Probar hacer el posicionamiento con Place

label_prev = Entry(root,width=15,font=("Copperplate Gothic Bold",34),relief="flat",justify=RIGHT)
label_prev.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

# Entry donde muestra los resultados.

label_next = Entry(root, width=15, font=("Copperplate Gothic Bold", 34), relief="flat")
label_next.grid(row=1,column=0,columnspan=3,padx=5,pady=5)

# Funciones

def mostrar(valor):
    text = label_prev.get()
    label_prev.delete(0,END)
    label_prev.insert(0, str(text) + str(valor))

def boton_igual():
    ecuacion = label_prev.get()
    try:
        ans= eval(ecuacion)
        label_next.delete(0,END)
        label_next.insert(0,str(ans))
    except:
        label_next.delete(0,END)
        label_next.insert(0,"Syntax Error.")

def borrar():
    label_prev.delete(0,END)
    label_next.delete(0,END)

# Botones
boton1 = Button(root,text="1",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(1))
boton1.grid(row=2,column=0)

boton2 = Button(root,text="2",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(2))
boton2.grid(row=2,column=1)

boton3 = Button(root,text="3",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(3))
boton3.grid(row=2,column=2)

boton4 = Button(root,text="4",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(4))
boton4.grid(row=3,column=0)

boton5 = Button(root,text="5",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(5))
boton5.grid(row=3,column=1)

boton6 = Button(root,text="6",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(6))
boton6.grid(row=3,column=2)

boton7 = Button(root,text="7",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(7))
boton7.grid(row=4,column=0)

boton8 = Button(root,text="8",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(8))
boton8.grid(row=4,column=1)

boton9 = Button(root,text="9",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(9))
boton9.grid(row=4,column=2)

botonac = Button(root,text="AC",relief="flat",background="DarkOrange2",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: borrar())
botonac.grid(row=5,column=0)

boton0 = Button(root,text="0",cursor="hand2",relief="flat",background="magenta3",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar(0))
boton0.grid(row=5,column=1)

botonXD = Button(root,text="XD",cursor="hand2",relief="flat",background="magenta3",width=4,height=2,font=("Copperplate Gothic Bold", 24),command=lambda: mostrar("XD"))
botonXD.grid(row=5,column=2)


root.mainloop()