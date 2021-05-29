################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 5 - Comparación de números
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej3 import ingreso_real
def signo(numero):
    if numero > 0:
        print("El numero es positivo!")
    elif numero < 0:
        print("El numero es negativo!")
    else:
        print("El numero es igual a 0!")       
    
    
def prueba():
    print("Programa que compara el signo de un numero")
    numero = ingreso_real("Ingrese un numero: ")
    signo(numero)
    pass

if __name__ == "__main__":
    prueba()
