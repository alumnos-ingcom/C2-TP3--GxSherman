################
# Germán Bernhard @GermanBernhard
# TP4 - Ejercicio 11 - Palíndromo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_palindromo(texto):

    igual = 0
    aux = 0
    for i in reversed(range(0, len(texto))):
        if texto[i].lower() == texto[aux].lower():
            igual += 1
            aux += 1
        
    if len(texto) == igual:
        return True
    else:
        return False

def prueba():
    texto = input("Ingrese una palabra o frase para determinar si es palindromo: ")
    if es_palindromo(texto):
        print(texto + " es palindromo")
    else:
        print(texto + " no es palindromo")


if __name__ == "__main__":
    prueba()