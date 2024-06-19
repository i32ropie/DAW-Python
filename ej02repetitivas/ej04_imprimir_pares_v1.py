"""
Escribir un programa que imprima todos los números pares entre dos números que
se le pidan al usuario.

Análisis
--------
Leemos un número. Si es impar, le sumo 1 y ya es par. Leemos el segundo número.
Escribo el número desde el primero hasta el segundo de dos en dos.

Datos de entrada: dos números.

Información de salida: Los números pares que hay entre los dos anteriores.
Variables: num,num1,num2 (entero).

Diseño
------
Leer num1,num2
Si num1 es mayor que num2 intercambio el valor de las variables
Si num1 es par -> num <-- num1 sino num <-- num1+1
Mientras num <= num2
    Escribir num
    num <-- num+2
FinMientras
"""
