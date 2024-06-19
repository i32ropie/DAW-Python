"""
Programa ej14_invertir_numero.py

Propósito: Dado un número de dos cifras este programa lo invierte.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Vamos a hacerlo de dos formas.

1ª forma:   Pasamos el número a entero y extraemos sus dos cifras con
            la división (1ª) y el resto (2ª) entre 10.
            Variables: number, digit1, digit2, invertido

2ª forma:   Tratamos el número como una cadena de caracteres y mediante
            "slicing" accedemos a las posiciones de su primera y segunda
            cifra.
            Variables: number, digit1, digit2, invertido
"""
