################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 7 - Restas sucesivas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):
    cociente = 0
    resto = dividendo
    while resto >= divisor:
        resto = resto - divisor
        cociente = cociente +1
    return (cociente, resto)
    if divisor == 0:
        return 0
    
def prueba():
    
    print("programa que calcula el cociente y resto de una division mediante restas sucesivas")
    dividendo = ingreso_entero("Ingrese el dividendo: ")
    divisor = ingreso_entero("Ingrese el divisor ")
    (cociente, resto) = division_lenta(dividendo, divisor)
    print(f"La división entre {dividendo} y {divisor} da {cociente} como cociente y {resto} como resto.")
    
    
if __name__ == "__main__":
    prueba()
