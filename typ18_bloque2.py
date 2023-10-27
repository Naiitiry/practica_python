#   --------------------- Centrar ventana ---------------------

# PRIMERA FORMA
from tkinter import *

# Ventana Principal
root=Tk()
root.title("Teoría 18, Bloque 2, Centrar Ventana")

#   -------     Método RESIZABLE(False,False)     -------

# root.resizable(False,True) 
# Modificar los valores booleanos nos permite modificar, manualmente, el ancho y/o alto
# ancho_ventana=500
# alto_ventana=400

# #   -------------- Pantalla --------------

# # Capturar alto y ancho de pantallas donde se ejecuta el programa
# # ya que mi pantalla es muy diferente a las demás.
# ancho_pantalla = root.winfo_screenwidth()
# alto_pantalla = root.winfo_screenheight()

# #   ------- Posicionamiento de la ventana del programa -------

# coordenadas_x = int((ancho_pantalla/2)-(ancho_ventana/2))
# coordenadas_y = int((alto_pantalla/2)-(alto_ventana/2))
# root.geometry("{}x{}+{}+{}".format(ancho_ventana,alto_ventana,coordenadas_x,coordenadas_y))
# Label(text=f'Ancho pantalla: {ancho_pantalla} píxeles').pack()
# Label(text=f'Alto pantalla: {alto_pantalla} píxeles').pack()

#   -------    Método MAximizar o minimizar ventana    -------

root.state("zoomed") #maximizar
# para ver las demás opciones hay que poner mal el string y te muestras las 4 opciones.

#   -------    Método GEOMETRY()    -------

# root.geometry()
# AJUSTE DE VENTANA Y PANTALLA
# root.eval('tk::PlaceWindow . center')
# eval: es una expresión que pasa una cadena de carácteres como código


# # ------- Widgets -------
# entrada = Entry(root).pack()
# # ------- Botón -------
# boton = Button(root,text="Enviar").pack()

root.mainloop()