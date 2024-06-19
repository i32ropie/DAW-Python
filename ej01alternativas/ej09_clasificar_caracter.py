"""
Programa: ej09_clasificar_caracter.py

Propósito: Lee un carácter de teclado y muestra por la pantalla el mensaje:

- «Es signo de puntuación» solo si el carácter leído es un signo de puntuación.
- «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada).
- «Es un dígito» si es un dígito.
- «Es otro carácter» si no es ninguno de los anteriores.
- «No es un carácter» si el usuario ha introducido más de un carácter.

Autoría: Clase de 1ºDAW-B.
Fecha: 28/10/2020
-----------------------------------------------------------------------------------
Algoritmo:
-----------------------------------------------------------------------------------
Variables:  ch (cadena de caracteres)

PEDIR ch
SI LONGITUD(ch) == 1
    SI es_signo_puntuación(ch)
        ESCRIBIR "Signo de puntuación"
    SINO SI es_letra(ch)
         ESCRIBIR "Es una letra"
    SINO SI es_digito(ch)
        ESCRIBIR "Dígito"
    SINO
        ESCRIBIR "Otro carácter"
    FIN-SI
SINO
    ESCRIBIR "No es un carácter"FIN-SI
"""
