################
# Germán Patricio Bernhard Bellini - @GermanBernhard
# Tp4ej1
# UNRN Andina - Introducción a la Ingenieria en Computación
################




def ingreso_entero(mensaje,):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    try:
        entero = int(input(mensaje + " #"))
        return entero, True
    except ValueError as e:
        print("Eso no era un numero")
        #raise IngresoIncorrecto("Eso no era un numero!") from e
        return 0, False
    
def ingreso_entero_reintento(mensaje, cantidad_reintentos):
    exito = False
    cantidad_intentos = 0
    while exito == False and cantidad_intentos < cantidad_reintentos:
        entero, exito = ingreso_entero(mensaje)
        cantidad_reintentos = cantidad_reintentos -1
    if cantidad_intentos == cantidad_reintentos:
        raise NoMasReintentos("Se quedó sin intentos")
    return entero
def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    pass
class NoMasReintentos(Exception):
    """Esta es la Excepcion para la falta de reintentos"""
    pass

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass
def prueba():
    entero = ingreso_entero_reintento("Ingrese un numero", 5)
    #entero = ingreso_entero("ingrese un numero")
    print(F"el numero ingresado es {entero}")  
    
if __name__ == "__main__":
     prueba()
 