################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 4 - Comparación de números
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Corregido retornar valores numericos en la funcion y imprimir en prueba

from tp4ej3 import ingreso_real

def compara(numero, otro_numero):
    
    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else :
       return 1
        
def prueba():
    
    print("Programa que compara dos valores de numeros")
    numero = ingreso_real("Ingrese el primer numero:")
    otro_numero = ingreso_real("Ingrese el segundo numero:")
    valor_final = compara(numero, otro_numero)
    print('', valor_final)
    


if __name__ == "__main__":
    prueba()
