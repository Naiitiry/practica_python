#           PRÁCTICA

class Motocicleta():
    # Atributo de Clase
    estado = "nueva"
    motor = False

    # Métodos
    def __init__(self,color,matricula,combustible_litros,numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso, combustible_maximo):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.combustible_maximo = combustible_maximo
    
    def arrancar(self):
        if self.motor:
            print("El motor ya estaba encendido.")
        else:
            print("Se arranca el motor, ya que estab apagado.")
    
    def apagar(self):
        if self.motor:
            print("El motor está prendido, se procede a apagarlo")
        else:
            print("El motor estaba apagado.")
    
    #Ejercicio 12
    def consultar_precio(self):
        print(f'El precio de la motocicleta {self.marca}, modelo {self.modelo} es de ${self.precio}')
    
    #Ejercicio 14
    def comprobar_tanque(self):
        print(f'*****Reporte de depósito de {self.marca} {self.modelo}*****')
        print(f'El tanque tiene {self.combustible_litros} litros.')
        print(f'La capacidad máxima del tanque es de {self.combustible_maximo}')
        print(f'Faltan {self.combustible_maximo - self.combustible_litros} para llenar el tanque')
        print(f'*****Fin del reporte*****\n')
    
    def llenar(self):
        while True:
            self.llenar_litros = float(input("Por favor, introduzca la cantidad de litros que desea rellenar: "))
            if self.combustible_litros + self.llenar_litros <= self.combustible_maximo:
                print("Llenado exitoso!.")
                print(f'Se ha llenado {self.llenar_litros} litros.')
                self.combustible_litros += self.llenar_litros
                print(f'El tanque tiene {self.combustible_litros} litros de combustible.')
                break
            else:
                print("No cabe tanto combustible. Rebalsará del tanque.")

moto_1 = Motocicleta("verde","ABC123",10,2,"Jonda","Chiwinchi","20/03/2022",350,55,17)

#Ejercicio 10
moto_1.precio = 50000

#Ejercicio 8
moto_2 = Motocicleta(
    matricula="DEF456",
    combustible_litros=0,
    color="Negra",
    marca="Joseso",
    modelo="Guernica",
    numero_ruedas=2,
    peso=350,
    fecha_fabricacion="25/05/2023",
    velocidad_punta=160,
    combustible_maximo=15
)
moto_1.comprobar_tanque()
moto_1.llenar()
moto_1.comprobar_tanque()
moto_1.llenar()

