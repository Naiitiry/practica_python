# Importación de funciones
from operaciones import suma,resta,multiplicacion,division,exponente,modulo
# se puede importar de varias formas: from operaciones import *, sería el más rápido

# Se da un título a la calculadora.
print("--- CALCULADORA MEJORADA DE NUEVO ---")

while True:
    # Se le pide al usuario que elija una opción y se evalúa
    print("Por favor, elija una opción:")
    print("1- Suma.")
    print("2- Resta.")
    print("3- Multiplicación.")
    print("4- División.")
    print("5- Módulo.")
    print("6- Exponente.")
    print("7- Salir.")

    # Se le pide al usuario un número de opción
    eleccion = int(input("Teclee un número y pulse ENTER:\n"))

    match eleccion:
        case 1:
            print('Ha elegido la opción "suma".')
        case 2:
            print('Ha elegido la opción "resta".')
        case 3:
            print('Ha elegido la opción "multiplicación".')
        case 4:
            print('Ha elegido la opción "división".')
        case 5:
            print('Ha elegido la opción "módulo".')
        case 6:
            print('Ha elegido la opción "exponente".')
        case 7:
            print('Saliendo de la calculadora...')
            break
        case _:
            print('Error, opción inválida. Especifique una opción del 1 al 7.')

    # Se solicitan los dos números para cualquier operación que elija.
    num1 = float(input("Especifique el primer operando:\n"))
    num2 = float(input("Especifique el segundo operando:\n"))
    
    match eleccion:
        case 1:
            resultado = suma.suma(num1, num2)
            print(f"El resultado de sumar {num1} + {num2} es: {resultado}.\n")
        case 2:
            resultado = round(resta.resta(num1, num2), 2)
            print(f"El resultado de restar {num1} - {num2} es: {resultado}.\n")
        case 3:
            resultado = round(multiplicacion.multiplicacion(num1, num2), 2)
            print(f"El resultado de multiplicar {num1} por {num2} es: {resultado}.\n")
        case 4:
            resultado = round(division.division(num1, num2), 2)
            print(f"El resultado de dividir {num1} entre {num2} es: {resultado}.\n")
        case 5:
            resultado = round(modulo.modulo(num1, num2), 2)
            print(f"El resto de la división de {num1} entre {num2} es: {resultado}.\n")
        case 6:
            resultado = round(exponente.exponente(num1, num2), 2)
            print(f"{num1} elevado a {num2} es: {resultado}.\n")