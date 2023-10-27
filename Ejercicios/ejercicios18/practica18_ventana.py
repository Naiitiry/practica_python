from tkinter import *
import tkinter.messagebox as msb
import random

# Mensaje de inicio del juego
msb.showinfo("Adivina el número.","Introduzca un número del 1 al 1000. ¿Cuántos intentos te costaran hasta acertar?.")

root=Tk()
root.title("Adivinanza")
root.resizable(False,False)
#-topmost es para que la ventana que ponemos los numeros estén delante de todas las ventanas.
root.attributes("-topmost",True)
ancho_ventana=400
alto_ventana=100

#Pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
coor_x = int((ancho_pantalla/2)-(ancho_ventana/2))
coor_y = int((alto_pantalla/2)-(alto_ventana/2))

root.geometry("{}x{}+{}+{}".format(ancho_ventana,alto_ventana,coor_x,coor_y))

# Entrada de datos
entrada = Entry(root)
entrada.insert(0,"Escriba un número")
entrada.bind("<Button-1>",lambda d : entrada.delete(0,END))
entrada.pack()

aleatorio = random.randint(1,1000)
intentos = 1
print(aleatorio)

# Función para ventanas de aviso.
def adivinanza():
    global intentos
    #Se obtiene el valor del Entry
    try:
        numero = int(entrada.get())
        if numero > aleatorio:
            msb.showinfo("¡Fallaste!",f"El número es menor. Introduce un número menor que {numero}.")
            intentos += 1
        elif numero < aleatorio:
            msb.showinfo("¡Fallaste!",f"El número es mayor. Introduce un número mayor que {numero}.")
            intentos += 1
        else:
            msb.showinfo("¡Excelente!",f'Adivinaste el número luego de {intentos} intentos.')
    except:
        msb.showerror("¡Error!","Valor no válido.")
        intentos+=1

boton = Button(root,text="Enviar",command=adivinanza)
boton.pack()

root.mainloop()