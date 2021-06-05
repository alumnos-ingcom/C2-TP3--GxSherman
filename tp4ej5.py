################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 5 - Comparación de números
# UNRN Andina - Introducción a la Ingenieria en Computación
################


#Corrección ahora retorna valor numerico en vez de print (1 si es positivo, -1 si es negativo y 0 si es este mismo)
from tp4ej3 import ingreso_real
def signo(numero):
    if numero > 0:
        return numero, 1
    elif numero < 0:
        return numero, -1
    else:
        return numero
    
    
def prueba():
    print("Programa que compara el signo de un numero")
    numero = ingreso_real("Ingrese un numero: ")
    resultado = signo(numero)
    print("Si el resultado es 1, sera positivo, y si es -1 sera negativo")
    print(f" El numero ingresado es {resultado} ")
    
  

if __name__ == "__main__":
    prueba()
