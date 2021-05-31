################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 9 - Números primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero


def es_primo(numero):
    for contador in range(numero):
        if contador+1 == numero:
            return True
        
        elif contador+1 == 1:
            pass
        
        else:
            resto = numero % (contador+1)
            if resto == 0:
                return False
    


def prueba():
    print("programa que marca si un numero es primo o no")
    numero = ingreso_entero("Ingrese un numero:")
    
    if numero < 0:
        print("Los numeros negativos no son primos.")
    elif es_primo(numero):
        print(f"{numero} es primo")
    elif numero == 1 or numero == 0:
        print("Recordemos que 0 y 1 no son primos!")

    else:
        print(f"{numero} no es primo.")

if __name__ == "__main__":
    prueba()