################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 2 - Suma Lenta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
 
from tp4ej1 import ingreso_entero
 
def suma_lenta(numero, otro_numero):
    if otro_numero > 0 :
        for i in range (0, otro_numero, 1) :
            numero = numero + 1
            print(f"{numero}")
    elif otro_numero < 0:    
        for i in range (-otro_numero) :
            numero = numero - 1
            print(f"{numero}")
    else : 
        print(f"{numero}")    
    

def prueba():
    
    print("Ejercicio 2 tp 4")
    print("Ingrese 2 numeros para sumarlos lentamente.")
    numero = ingreso_entero("Ingrese un numero:")
    otro_numero = ingreso_entero("Ingrese otro numero:")
    suma_lenta(numero, otro_numero) 
    pass

if __name__ == "__main__":
    prueba()