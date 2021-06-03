################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 8 - Ordenar 3 valores
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej6 import maximo
from tp4ej6 import minimo


def ordenar_mayor_a_menor(uno, dos, tres):
    a = minimo((uno, dos, tres))
    c = maximo((uno, dos, tres))
    b = (uno + dos + tres) - a - c

    return c, b, a
    
def ordenar_menor_a_mayor(uno, dos, tres):
    a = minimo((uno, dos, tres))
    c = maximo((uno, dos, tres))
    b = (uno + dos + tres) - a - c

    return a, b, c

def prueba():
    
    uno = int(input("Escriba el primer numero: "))
    dos = int(input("Escriba el segundo numero: "))
    tres = int(input("Escriba el tercer numero: "))
    menor_mayor = ordenar_menor_a_mayor(uno, dos, tres)
    mayor_menor = ordenar_mayor_a_menor(uno, dos, tres)
    print(f"El orden de menor a mayor es {menor_mayor}")
    print(f"El orden de mayor a menor es {mayor_menor}")

if __name__ == "__main__":
    prueba()
