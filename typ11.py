"""     POO     """
"""
class Taza():
    # Atributos (variables dentro de una clase)
    color = "blanco"
    mensaje = None
    material = "Porcelana"
    limpia = True

    # Métodos (funciones de una clase)


# Instanciación de la clase
taza_1 = Taza()
taza_2 = Taza()

taza_2.color = "Blanco y azul"

print(taza_1.color)
print(taza_2.color)
"""
"""
# Se declara la clase 'Vehiculo'
class Vehiculo():
    # Atributos
    # __init__ es un método para generar atributos
    def __init__(self,color,longitud_metros,ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    # Métodos
    def arrancar(self):
        print("El vehículo ha arrancado.")
    
    def detener(self):
        print("El vehículo está detenido.")
    
    def mostrar_info(self):
        print(f'Vehículo de color {self.color}, largo de {self.longitud_metros} mts y de {self.ruedas} ruedas')

vehiculo_1 = Vehiculo("rojo",4,4)
vehiculo_2 = Vehiculo("verde",15,8)

# Crear atributo fuera de la clase.
#vehiculo_2.material_aleron = "Fibra de carbono"
#print(vehiculo_2.material_aleron)

# Llamadas a métodos.
#vehiculo_1.arrancar()
#vehiculo_1.detener()
vehiculo_1.mostrar_info()
vehiculo_2.mostrar_info()
"""
