import random
from tkinter import *

# Debemos crear una variable con un número aleatorio, lo tomará de referencia.
num = random.randint(1,1000)
# pedimos que ingresen un número
usuario = int(input("Ingrese un número del 1 al 1000: "))
intento = 0
# Bucle indeterminado para verificar si acertó o no, puede hacer un montón de intentos.
while True:
    if num == usuario:
        print("Genial, acertaste!")
        intento+=1
        print(f'Intentos: {intento}')
        break
    elif num<usuario:
        print(f"El número {usuario} es mayor que el aleatorio, intenta de nuevo: ")
        usuario = int(input(f"Ingrese un número menor de {usuario}: "))
        intento+=1
    elif num>usuario:
        print(f"El número {usuario} es menor que el aleatorio, intenta de nuevo: ")
        usuario = int(input(f"Ingrese un número mayor de {usuario}: "))
        intento+=1