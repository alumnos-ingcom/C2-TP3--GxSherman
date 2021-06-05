################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 6 - Máximo / Mínimo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


from tp4ej1 import ingreso_entero



def maximo(lista):
    
    maximo = lista[0]
    
    for i in range(0, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

def minimo(lista):
    
    minimo = lista[0]
    
    for i in range(0, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

def construccion_lista ():
    lista=[]
    for i in range(5):
        numero = ingreso_entero("Ingrese un valor que sera sumado a la lista")
        lista.append(numero)
    return lista

def prueba():
    print("programa que muestra valor maximo y minimo de una lista")
    lista = construccion_lista()
    valor_min = minimo(lista)
    valor_max = maximo(lista)
    
    print("\nLos valores maximos y minimos de la lista son: ")
    print("Minimo:", valor_min)
    print("Maximo:", valor_max)
    

if __name__ == "__main__":
    prueba()

