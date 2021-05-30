################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 3 - Conversión de temperaturas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import IngresoIncorrecto

def ingreso_real(mensaje):
    ingreso = input(mensaje + ' #')
    try:
        real = float(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero valido!") from err
    return real

def convertir_a_centigrados(fahrenheit):
    conversion = (fahrenheit - 32) * 5/9
    return conversion

def convertir_a_fahrenheit(centigrados):
    conversion = (centigrados * 9/5) + 32
    return conversion

def prueba():
    print(" Programa para convertir grados °c a °f y viceversa")
    tipo_conversion = ingreso_real(" si ingresa '1' convierte de °f a °c\n si ingresa '2' convierte de °c a °f ")
    if int(tipo_conversion) == 1:
        fahrenheit = ingreso_real("Ingrese los grados Fahrenheit que desee convertir")
        resultado = convertir_a_centigrados(fahrenheit)
        print ('Celsius: ', resultado)
        
        
    elif int(tipo_conversion) == 2:
        centigrados = ingreso_real("Ingrese los grados Celsius que desee convertir:")
        resultado = convertir_a_fahrenheit(centigrados)
        print ('Fahrenheit: ', resultado)
    else :
        print("No se ingreso ni 1 ni 2, ingrese nuevamente")
        
if __name__ == "__main__":
    prueba()