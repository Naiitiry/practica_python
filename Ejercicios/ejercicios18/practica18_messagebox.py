#importaciones
import tkinter.messagebox as msb
# nos permite guardar, en una variable, el resultado queda en consola, dependiendo de la alerta cambia el aviso.
# valor = msb.showinfo("Hola bo","Probando en consola el messagebox")

valor2 = msb.askyesnocancel("Hola bo","Probando en consola el messagebox")
if valor2:
    print("El usuario ha pulsado el botón 'Sí'.")
elif valor2 is False:
    print("El usuario ha pulsado el botón 'No'.")
else:
    print("El usuario ha pulsado el botón 'Cancelar'.")