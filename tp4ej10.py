################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 10 - Factores Primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej9 import es_primo
from tp4ej1 import ingreso_entero


def factores_primos(numero):
    n_primos = []
    for contador in range(2, numero + 1):
        while numero % contador == 0:
            n_primos.append(contador)
            numero = numero / contador
            
    return tuple(n_primos)

def prueba():
    print("programa que calcula los factores primos de un numero")
    numero = ingreso_entero("Ingrese un numero entero positivo: ")
    if es_primo(numero):
        print(f"{numero} es primo, es decir no se puede descomponer en factores primos")
    else:
        n_primos = factores_primos(numero)
        print(f"Los factores primos de {numero} son {n_primos}")
    
    
if __name__ == "__main__":
    prueba()