################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 1 - Ingreso de números enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
        return entero
    except ValueError as err:
        raise IngresoIncorrecto(f"'{ingreso}' no era un numero!!!")
    return entero 

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
  
    intentos = cantidad_reintentos
   
    while cantidad_reintentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:
            print(f"No era un número, quedan {cantidad_reintentos}")
            cantidad_reintentos = cantidad_reintentos -1
    raise IngresoIncorrecto(f"luego de {intentos}")

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    
    entero = ingreso_entero(mensaje)
    try:
        if entero >= valor_minimo and entero <= valor_maximo:
            return entero
        else:
            raise FueraDeRango("El numero ingresado está fuera del rango determinado.")
            pass
    except TypeError as err:
        raise TypeError("Los valores ingresados no eran numeros, ingrese un numero por favor") from err
    


class FueraDeRango(Exception):
    """Esta es la Excepcion para cuando se ingresa un número fuera del rango establecido por el usuario"""
    pass

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass


def prueba():
    print("Programa que determina si un numero es entero o no")
    mensaje = "Ingrese un numero"
    valor_minimo = ingreso_entero("Ingrese el valor minimo")
    valor_maximo = ingreso_entero("Ingrese el valor maximo")
    numero_entero = ingreso_entero_restringido(mensaje,valor_minimo,valor_maximo)

    print(F"el numero que ingreso es {numero_entero}")


if __name__ == "__main__":
    prueba()
    