"""
multiplicacion = lambda numero1,numero2: numero1*numero2

resultado1 = multiplicacion(3,4)
resultado2 = multiplicacion(7,4)
print(resultado1)
print(resultado2)
"""
#Otra manera de mostrar la función lambda
# (lambda numero1,numero2: print(numero1*numero2))(4,5)

#Calcular el área de un círculo
'''
radio_cm = int(input("Ingrese el rádio del círculo en cm.\n"))
pi = 3.1416
calcular_area = lambda radio: pi * radio * radio
area = round(calcular_area(radio_cm),2)
print(f'El área del cículo es de {area} cm.')
'''
colores = ['rojo','azul','verde','naranja']
(lambda color:print(f'El color se encuentra en la posición {colores.index(color)} de la lista'))("azul")