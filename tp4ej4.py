################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 4 - Comparación de números
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej3 import ingreso_real

def compara(numero, otro_numero):
    
    if numero < otro_numero:
        print("-1, es decir, el segundo numero es mayor que el primero")
    elif numero == otro_numero:
        print("0, son iguales los numeros!")
    else :
        print("1, es decir, el primer numero es mayor que el segundo")
        
def prueba():
    
    print("Programa que compara dos valores de numeros")
    numero = ingreso_real("Ingrese el primer numero:")
    otro_numero = ingreso_real("Ingrese el segundo numero:")
    compara(numero, otro_numero)
    pass

if __name__ == "__main__":
    prueba()
