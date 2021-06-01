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
    try:
        entero = int(input(mensaje + " #"))
        return entero
    except ValueError as e:
        print(IngresoIncorrecto("Eso no era un numero, por favor ingrese un numero!!"))
        return None

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
  
    cantidad_intentos = 0
    entero = None
    while entero == None and cantidad_intentos < cantidad_reintentos:
        entero = ingreso_entero(mensaje)
        cantidad_reintentos = cantidad_reintentos - 1
        if entero == None:
            print(F"Le quedan {cantidad_reintentos} intentos para ingresar numeros.\n")
    if cantidad_intentos == cantidad_reintentos:
        raise No_Mas_Reintentos("Se quedó sin intentos, reinicie el programa")
    return entero


def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    
    entero = ingreso_entero(mensaje)
    try:
        if entero >= valor_minimo and entero <= valor_maximo:
            return entero
        else:
            raise Fuera_De_Rango("El numero ingresado está fuera del rango determinado.")
            pass
    except TypeError as e:
        raise TypeError("Los valores ingresados no eran numeros, ingrese un numero por favor") from e
    
class No_Mas_Reintentos(Exception):
    """Esta es la Excepcion para la falta de reintentos"""
    pass

class Fuera_De_Rango(Exception):
    """Esta es la Excepcion para cuando se ingresa un número fuera del rango establecido por el usuario"""
    pass

class Ingreso_Incorrecto(Exception):
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
    